import {get, writable} from "svelte/store";
import {attributeDTOExtendedList} from "../dto/AttributeDTOExtended";


export const isEditingNewAttribute = writable(false)
export const isEditingNewAttributeValue = writable(false)
export const expandAttributeStore = writable([])
export const isEditingAttributeStore = writable([])


export const setExpandAttributeStore = function() {
    const currentExpandId = getCurrentAttributeExpandId()
    if(typeof currentExpandId !== "undefined") {
        expandAttributeStore.set(get(attributeDTOExtendedList)
            .map(x => x.attribute.id === currentExpandId ?
                ({attribute: x.attribute, isExpanded: true}) :
                ({attribute: x.attribute, isExpanded: false})))
    }else{
        expandAttributeStore.set(get(attributeDTOExtendedList).map(x => ({attribute: x.attribute, isExpanded: false})))
    }
}

export const setIsEditingAttributeStore = function() {
    const currentEditingId = getCurrentAttributeEditingId()
    if(typeof currentEditingId !== "undefined") {
        isEditingAttributeStore.set(get(attributeDTOExtendedList)
            .map(x => x.attribute.id === currentEditingId ?
                ({attribute: x.attribute, isEditing: true}) :
                ({attribute: x.attribute, isEditing: false})))
    }else{
        isEditingAttributeStore.set(get(attributeDTOExtendedList).map(x => ({attribute: x.attribute, isEditing: false})))
    }
}

export const getCurrentAttributeEditingId = function() {
    const tempFiltered = get(isEditingAttributeStore).filter(x => x.isEditing)
    if(tempFiltered.length == 1) {
        return tempFiltered[0].attribute.id
    }else{
        return undefined
    }
}

export const getCurrentAttributeExpandId = function() {
    const tempFiltered = get(expandAttributeStore).filter(x => x.isExpanded)
    if(tempFiltered.length == 1) {
        return tempFiltered[0].attribute.id
    }else{
        return undefined
    }
}


export const isEditingNameByAttribute = function(attributeDefinitionId:string) {
    if(get(isEditingAttributeStore).length > 0) {
        const temp = get(isEditingAttributeStore).find(x => x.attribute.id == attributeDefinitionId)
        if(typeof temp !== "undefined") {
            return temp.isEditing
        }
    }else{
        return false
    }
}

export const isExpandedByAttribute = function(attributeDefinitionId:string) {
    if(get(expandAttributeStore).length > 0) {
        const temp = get(expandAttributeStore).find(x => x.attribute.id == attributeDefinitionId)
        if(typeof temp !== "undefined") {
            return temp.isExpanded
        }
    }else{
        return false
    }

}

export const setAllExpandedAttributesFalse = function() {
    get(expandAttributeStore).forEach(x => x.isExpanded = false)
    expandAttributeStore.set(get(expandAttributeStore))
}

export const setExpandedAttributeTrue = function(attributeDefinitionId:string) {
    get(expandAttributeStore).forEach(x => {
        x.isExpanded = x.attribute.id === attributeDefinitionId;
    })
    expandAttributeStore.set(get(expandAttributeStore))

}

export const setAllEditingAttributesFalse = function() {
    get(isEditingAttributeStore).forEach(x => x.isEditing = false)
    isEditingAttributeStore.set(get(isEditingAttributeStore))
}

export const setEditingAttributeTrue = function(attributeDefinitionId:string) {
    get(isEditingAttributeStore).forEach(x => {
        x.isEditing = x.attribute.id === attributeDefinitionId;
    })
    isEditingAttributeStore.set(get(isEditingAttributeStore))
}

export const setEditingAttributeFalse = function(attributeDefinitionId:string) {
    get(isEditingAttributeStore).forEach(x => {
        if(x.attribute.id === attributeDefinitionId) {
            x.isEditing = false
        }
    })
    isEditingAttributeStore.set(get(isEditingAttributeStore))
}