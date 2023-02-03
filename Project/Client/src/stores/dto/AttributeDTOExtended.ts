import type {AttributeDefinition} from "../model/AttributeDefinition";
import type {AttributeValue} from "../model/AttributeValue";
import {derived, get, writable, type Writable, type Readable} from "svelte/store";

export class AttributeDTOExtended {
    attribute: AttributeDefinition
    values: Array<AttributeValue>

    constructor(attribute: AttributeDefinition, values: Array<AttributeValue>) {
        this.attribute = attribute;
        this.values = values;
    }
}

export const attributeDTOExtendedList : Writable<Array<AttributeDTOExtended>> = writable([])

export const setAttributeDTOExtendedList = function (newList:Array<AttributeDTOExtended>) {
    attributeDTOExtendedList.set(newList)
}

export const attributeValueList:Readable<Array<AttributeValue>> = derived(attributeDTOExtendedList,
    () => get(attributeDTOExtendedList).map(x => x.values).flat()
)

export const attributeDefinitionList:Readable<Array<AttributeDefinition>> = derived(attributeDTOExtendedList,
    () => get(attributeDTOExtendedList).map(x => x.attribute)
)

export const getMissingAttributeValues = function (attributeDefinitionId: string, attributeValueList: Array<AttributeValue>) {
        const currentAttributeValueIdList:Array<string> = attributeValueList.map(x=>x.id)
        return derived(attributeDTOExtendedList, () =>
            get(attributeDTOExtendedList)
            .filter(x => x.attribute.id == attributeDefinitionId)
            .map(x => x.values)
            .flat()
            .filter(y => currentAttributeValueIdList.indexOf(y.id) == -1))
}

export const getMissingAttributeDefinitionsMin1Values = function (currentAttributeDefinitionList: Array<AttributeDTOExtended>) {
        if(typeof currentAttributeDefinitionList == "undefined") {
            return get(attributeDTOExtendedList).filter(x => x.values.length > 0).map(x => x.attribute)
        }else{
            const mappedCurrAttributeDefinitionList = currentAttributeDefinitionList.map(x => x.attribute).map(z => z.id)
            return get(attributeDTOExtendedList)
                .filter(x => typeof x.values === "undefined" ? false : x.values.length > 0)
                .map(x => x.attribute)
                .filter(y => mappedCurrAttributeDefinitionList.indexOf(y.id) == -1)
        }

}

export const getAttributeDefinitionById = function(id:string) {
    return get(attributeDefinitionList).find(x => x.id === id)
}

export const getAttributeDTOExtendedById = function (attributeId:string) {
    return get(attributeDTOExtendedList).find(x => x.attribute.id === attributeId)
}

export const addNewAttributeToDTOExtendedList = function (attribute:AttributeDefinition) {
    const tempAttributeListDTOExtend = get(attributeDTOExtendedList)
    const newAttributeDTO = new AttributeDTOExtended(attribute, [])
    tempAttributeListDTOExtend.unshift(newAttributeDTO)
    attributeDTOExtendedList.set(tempAttributeListDTOExtend)
    console.log(get(attributeDTOExtendedList))
}

export const updateAttributeFromDTOExtendedList = function (attribute:AttributeDTOExtended) {
    const tempAttributeListDTOExtend = get(attributeDTOExtendedList)
    const tempAttributeIndex:number = tempAttributeListDTOExtend.indexOf(tempAttributeListDTOExtend.find(x => x.attribute.id === attribute.attribute.id))
    tempAttributeListDTOExtend[tempAttributeIndex] = attribute
    attributeDTOExtendedList.set(tempAttributeListDTOExtend)
}

export const removeAttributeFromDTOExtendedList = function (id:string) {
    const tempAttributeListDTOExtended = get(attributeDTOExtendedList).filter(x => x.attribute.id !== id)
    attributeDTOExtendedList.set(tempAttributeListDTOExtended)
}

export const deleteAttributeValueFromDTOExtendedList = function (delAttributeId:string, delId:string) {
    const tempAttributeListDTOExtended = get(attributeDTOExtendedList)
    const tempAttributeDefinition = tempAttributeListDTOExtended.find(x => x.attribute.id === delAttributeId)
    tempAttributeDefinition.values = tempAttributeDefinition.values.filter(x => x.id !== delId)
    attributeDTOExtendedList.set(tempAttributeListDTOExtended)
}

export const addAttributeValueToDTOExtendedList = function(attribute_id:string, attributeValue:AttributeValue) {
    const tempAttributeListDTOExtended = get(attributeDTOExtendedList)
    const tempAttributeDefinition = tempAttributeListDTOExtended.find(x => x.attribute.id === attribute_id)
    if(typeof tempAttributeDefinition.values === "undefined") {
        tempAttributeDefinition.values = []
    }
    tempAttributeDefinition.values.push(attributeValue)
    attributeDTOExtendedList.set(tempAttributeListDTOExtended)
}

export const filterAttributeDTOExtendedList = function(searchString:string) {
    if(searchString.length === 0) {
        return get(attributeDTOExtendedList)
    }

    const searchLowerCase = searchString.toLowerCase()
    const filtered = get(attributeDTOExtendedList).filter(x => {
            if(x.attribute.name.toLowerCase().includes(searchLowerCase)) {
                return true
            }
            return false
        }
    )
    return filtered
}

