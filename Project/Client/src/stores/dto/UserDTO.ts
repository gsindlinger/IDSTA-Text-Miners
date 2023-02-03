import type {User} from "../model/User";
import {writable,type Writable} from "svelte/store";

export class UserDTO {
    user: User
    attributes: Array<string>

    constructor(user: User, attributes: Array<string>) {
        this.user = user;
        this.attributes = attributes;
    }
}

export const userDTOList : Writable<Array<UserDTO>> = writable([])

export const setUserDTOList = function (newList:Array<UserDTO>) {
    userDTOList.set(newList)
}