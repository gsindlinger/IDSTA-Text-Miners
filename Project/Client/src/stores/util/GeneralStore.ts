import {writable} from "svelte/store";

export const isConnected = writable(true)
export const errorMessage = writable("")
export const isLoading = writable(false)


// enum and variable for the selected area at the navbar
export enum Topic{
    User,
    Attributes
}
export const selectedTopic = writable(Topic.User)