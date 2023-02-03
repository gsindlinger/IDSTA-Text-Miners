import Api from "./Api";
import {attribute_value_user_attribute, extended, user, users_all} from "./ApiStrings";
import type {UserDTO} from "../stores/dto/UserDTO";
import type {User} from "../stores/model/User";

export class UserApi {

    static getUserList = async () : Promise<any> => {
            const response = await Api.get(users_all);
            return response;
    };

    static getUserListExtended = async () : Promise<any> => {
            const response = await Api.get(users_all + extended);
            return response;
    };

    static getUserById = async(id:string) : Promise<any> => {
            const response = await Api.get(user + "/" + id);
            return response.results;
    };

    static getUserByIdExtended = async(id:string) : Promise<any> => {
            const response = await Api.get(user + "/" + id + extended);
            return response;
    }

    static addUser = async(newUser:User) : Promise<any> => {
            const response = await Api.post(user, JSON.stringify(newUser));
            return response;
    }

    static updateUserByIdExtended = async(id, userDTO:UserDTO) : Promise<any> => {
            const response = await Api.put(user + "/" + id, JSON.stringify(userDTO));
            return response;
    }

    static updateUserById = async(id:string, editedUser:User) : Promise<any> => {
        const response = await Api.put(user + "/" + id, JSON.stringify(editedUser));
        return response;
    }



    static deleteUserById = async(id:string) : Promise<any> => {
            const response = await Api.delete(user + "/" + id);
            return response;
    }

    static addUserAttributeValue = async(userId:string, attributeValueId:string) => {
        const response = await Api.post(user + "/" + userId + attribute_value_user_attribute + attributeValueId, "");
        return response;
    }

    static deleteUserAttributeValue = async(userId:string, attributeValueId:string) => {
        const response = await Api.delete(user + "/" + userId + attribute_value_user_attribute + attributeValueId);
        return response;
    }
    
}

