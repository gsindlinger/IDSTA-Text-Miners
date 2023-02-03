import type {AttributeDefinition} from "../model/AttributeDefinition";
import {writable,type Writable} from "svelte/store";

export class AttributeDTO{
    attribute: AttributeDefinition
    values: Array<string>
}

export const attributeDTOList : Writable<Array<AttributeDTO>> = writable([])

export const setAttributeDTOList = function (newList:Array<AttributeDTO>) {
    attributeDTOList.set(newList)
}