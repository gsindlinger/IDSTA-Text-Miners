import {get, writable} from "svelte/store";
import {userDTOExtendedList} from "../dto/UserDTOExtended";


export const isEditingNewUser = writable(false)
export const expandUserStore = writable([])
export const isEditingStore = writable([])


export const setExpandUserStore = function() {
    const currentExpandId = getCurrentUserExpandId()
    if(typeof currentExpandId !== "undefined") {
        expandUserStore.set(get(userDTOExtendedList)
            .map(x => x.user.id === currentExpandId ?
                ({user: x.user, isExpanded: true}) :
                ({user: x.user, isExpanded: false})))
    }else{
        expandUserStore.set(get(userDTOExtendedList).map(x => ({user: x.user, isExpanded: false})))
    }
}

export const setIsEditingUserStore = function() {
    const currentEditingId = getCurrentUserEditingId()
    if(typeof currentEditingId !== "undefined") {
        isEditingStore.set(get(userDTOExtendedList)
            .map(x => x.user.id === currentEditingId ?
                ({user: x.user, isEditing: true}) :
                ({user: x.user, isEditing: false})))
    }else{
        isEditingStore.set(get(userDTOExtendedList).map(x => ({user: x.user, isEditing: false})))
    }
}

export const getCurrentUserEditingId = function() {
    const tempFiltered = get(isEditingStore).filter(x => x.isEditing)
    if(tempFiltered.length == 1) {
        return tempFiltered[0].user.id
    }else{
        return undefined
    }
}

export const getCurrentUserExpandId = function() {
    const tempFiltered = get(expandUserStore).filter(x => x.isExpanded)
    if(tempFiltered.length == 1) {
        return tempFiltered[0].user.id
    }else{
        return undefined
    }
}


export const isEditingNameByUser = function(userId:string) {
    if(get(isEditingStore).length > 0) {
        const temp = get(isEditingStore).find(x => x.user.id == userId)
        if(typeof temp !== "undefined") {
            return temp.isEditing
        }
    }else{
        return false
    }
}

export const isExpandedByUser = function(userId:string) {
    if(get(expandUserStore).length > 0) {
        const temp = get(expandUserStore).find(x => x.user.id == userId)
        if(typeof temp !== "undefined") {
            return temp.isExpanded
        }
    }else{
        return false
    }

}

export const setAllExpandedUsersFalse = function() {
    get(expandUserStore).forEach(x => x.isExpanded = false)
    expandUserStore.set(get(expandUserStore))
}

export const setExpandedUserTrue = function(userId:string) {
    get(expandUserStore).forEach(x => {
        x.isExpanded = x.user.id === userId;
    })
    expandUserStore.set(get(expandUserStore))

}

export const setAllEditingUsersFalse = function() {
    get(isEditingStore).forEach(x => x.isEditing = false)
    isEditingStore.set(get(isEditingStore))
}

export const setEditingUserTrue = function(userId:string) {
    get(isEditingStore).forEach(x => {
        x.isEditing = x.user.id === userId;
    })
    isEditingStore.set(get(isEditingStore))
}

export const setEditingUserFalse = function(userId:string) {
    get(isEditingStore).forEach(x => {
        if(x.user.id === userId) {
            x.isEditing = false
        }
    })
    isEditingStore.set(get(isEditingStore))
}