import type {User} from "../model/User";
import {AttributeDTOExtended, attributeDTOExtendedList, getAttributeDefinitionById} from "./AttributeDTOExtended";
import {derived, get, type Readable, writable, type Writable} from "svelte/store";
import type {AttributeValue} from "../model/AttributeValue";
import {attributeValueList} from "./AttributeDTOExtended";

export class UserDTOExtended {
    user: User
    all_attributes: Array<AttributeDTOExtended>

    constructor(user: User, all_attributes: Array<AttributeDTOExtended>) {
        this.user = user;
        this.all_attributes = all_attributes;
    }
}

export const userDTOExtendedList:Writable<Array<UserDTOExtended>> = writable([])

export const setUserDTOExtendedList = function (newList:Array<UserDTOExtended>) {
    newList.forEach(x => typeof x.all_attributes === "undefined" ? x.all_attributes = [] : {})
    userDTOExtendedList.set(newList)
}

export const userList:Readable<Array<User>> = derived(userDTOExtendedList,
    () => {
        return get(userDTOExtendedList).map(x => x.user)
    })

export const getAttributesByUserId = function (id:string) {
    const tempAttributes = get(userDTOExtendedList).find(x => x.user.id == id)
    if(typeof tempAttributes === 'undefined') {
        return []
    }else{
        if(typeof tempAttributes.all_attributes == "undefined") {
            return []
        }else{
            return tempAttributes.all_attributes
        }
    }
}


export const getAttributeValueListByUserId = function (id:string) {
    return get(userDTOExtendedList)
        .find(x => x.user.id = id)
        .all_attributes
        .map(x => x.values.map(x => x.id))
        .flat()
}

export const removeUserFromDTOExtendedList = function(userId: string) {
    const tempUserListDTOExtended = get(userDTOExtendedList).filter(x => x.user.id != userId)
    userDTOExtendedList.set(tempUserListDTOExtended)
}

export const removeUserAttributeFromDTOExtendedList = function (userId:string, attributeValueId:string) {
    const tempUserListDTOExtended = get(userDTOExtendedList)
    const tempUserAttributes = tempUserListDTOExtended.find(x => x.user.id == userId).all_attributes
    tempUserAttributes.forEach(x => {
        x.values = x.values.filter(z => z.id !== attributeValueId)})
    tempUserListDTOExtended.forEach(x => {
        if(typeof x.all_attributes !== "undefined") {
            x.all_attributes = x.all_attributes.filter(x => x.values.length != 0)
        }
    })
    userDTOExtendedList.set(tempUserListDTOExtended)
}

export const addUserAttributeToDTOExtendedList = function(userId:string, attributeDefinitionId:string, attributeValueId:string) {
    const attributeValueToAdd:AttributeValue = get(attributeValueList).find(x => x.id == attributeValueId)
    const tempUserListDTOExtended = get(userDTOExtendedList)
    let tempUserAttributeDefinitionList:Array<AttributeDTOExtended> = tempUserListDTOExtended.find(x => x.user.id == userId).all_attributes
    if(typeof tempUserAttributeDefinitionList === "undefined") {
        tempUserAttributeDefinitionList = []
    }
    const tempUserAttributeDefinition:AttributeDTOExtended = tempUserAttributeDefinitionList.find(x => x.attribute.id == attributeDefinitionId)
    if(typeof tempUserAttributeDefinition === "undefined") {
        const newAttributeDefinition = getAttributeDefinitionById(attributeDefinitionId)
        tempUserAttributeDefinitionList.push(new AttributeDTOExtended(newAttributeDefinition, [attributeValueToAdd]))
    }else{
        tempUserAttributeDefinition.values.push(attributeValueToAdd)
    }
    userDTOExtendedList.set(tempUserListDTOExtended)
}

export const updateUserFromDTOExtendedList = function (editedUser:User) {
    const tempUserListDTOExtended = get(userDTOExtendedList)
    const tempUserIndex:number = tempUserListDTOExtended.indexOf(tempUserListDTOExtended.find(x => x.user.id == editedUser.id))
    tempUserListDTOExtended[tempUserIndex].user = editedUser
    userDTOExtendedList.set(tempUserListDTOExtended)
}

export const addNewUserToDTOExtendedList = function (newUser:User) {
    const tempUserListDTOExtended = get(userDTOExtendedList)
    const newUserDTO:UserDTOExtended = new UserDTOExtended(newUser, [])
    tempUserListDTOExtended.unshift(newUserDTO)
    userDTOExtendedList.set(tempUserListDTOExtended)
}

export const getUserDTOExtendedById = function (userId:string) {
    return get(userDTOExtendedList).find(x => x.user.id === userId)
}

export const removeAttributeFromUserDTOExtendedList = function (attributeId:string) {
    const tempUserListDTOExtended = get(userDTOExtendedList)
    tempUserListDTOExtended.forEach(x => x.all_attributes = x.all_attributes.filter(y => y.attribute.id !== attributeId))
    userDTOExtendedList.set(tempUserListDTOExtended)
}

export const deleteAttributeValueFromUserDTOExtendedList = function (attributeId:string, attributeValueId:string) {
    const tempUserListDTOExtended = get(userDTOExtendedList)
    tempUserListDTOExtended
        .forEach(x => {
            x.all_attributes.forEach(y => y.values = y.values.filter(z => z.id !== attributeValueId))
            x.all_attributes = x.all_attributes.filter(y => y.values.length > 0)
        })
    userDTOExtendedList.set(tempUserListDTOExtended)
}

export const updateAttributeFromUserDTOExtendedList = function (editedAttributeDTOExtended:AttributeDTOExtended) {
    const tempUserListDTOExtended = get(userDTOExtendedList)
    tempUserListDTOExtended
        .forEach(user => user.all_attributes
            .forEach(attr => {
                if(attr.attribute.id === editedAttributeDTOExtended.attribute.id) {
                    attr.attribute = editedAttributeDTOExtended.attribute
                    attr.values = attr.values.map(z => {
                            const tempIndex = editedAttributeDTOExtended.values.findIndex(a => a.id === z.id)
                            if(tempIndex > -1) {
                                return editedAttributeDTOExtended.values[tempIndex]
                            }else{
                                return z
                            }
                        })
                }
            }))
    userDTOExtendedList.set(tempUserListDTOExtended)

}

export const filterUserDTOExtendedList = function(searchString:string) {
    if(searchString.length === 0) {
        return get(userDTOExtendedList)
    }

    const searchLowerCase = searchString.toLowerCase()
    const filtered = get(userDTOExtendedList).filter(x => {
            if(x.user.name.toLowerCase().includes(searchLowerCase)) {
                return true
            }
            return false
        }
    )
    return filtered
}