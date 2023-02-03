//Copied and modified by https://dev.to/lukocastillo/svelte-3-how-to-connect-your-app-with-a-rest-api-axios-2h4e


// Api.js
import axios, { type AxiosInstance, type Method } from "axios";
import {base} from "./ApiStrings";

// Create an instance of axios to use the same base url.
const axiosAPI:AxiosInstance = axios.create({
    baseURL : base // it's not recommended having this info here.
});

// implement a method to execute all the request from here.
const apiRequest = (method:Method, url:string, request?: string) : Promise<any>|Promise<never> => {
    const headers = {
        authorization: "",
        'content-type': 'application/json'
    };
    //using the axios instance to perform the request that received from each http method
    return axiosAPI({
        method,
        url,
        data: request,
        headers
    }).then(res => {
        return Promise.resolve(res.data);
    })
        .catch(err => {
            return Promise.reject(err);
        });
};

// function to execute the http get request
const get = (url: string, request?: string) : Promise<any>|Promise<never> => apiRequest("get",url,request);

// function to execute the http delete request
const deleteRequest = (url: string, request?: string) : Promise<any>|Promise<never> =>  apiRequest("delete", url, request);

// function to execute the http post request
const post = (url: string, request: string) : Promise<any>|Promise<never> => apiRequest("post", url, request);

// function to execute the http put request
const put = (url: string, request: string) : Promise<any>|Promise<never> => apiRequest("put", url, request);

// expose your method to other services or actions
const API ={
    get,
    delete: deleteRequest,
    post,
    put,
};

export default API;