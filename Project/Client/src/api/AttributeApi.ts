import Api from "./Api"
import {attribute, attributes_all, extended, attrValue} from "./ApiStrings";
import type {AttributeDefinition} from "../stores/model/AttributeDefinition";
import type {AttributeValue} from "../stores/model/AttributeValue";
import type {AttributeDTOExtended} from "../stores/dto/AttributeDTOExtended";

export class AttributeApi {
    static getAttributeList = async () : Promise<any> => {
            const response = await Api.get(attributes_all);
            return response;
    };

    static getAttributeListExtended = async () : Promise<any> => {
            const response = await Api.get(attributes_all + extended);
            return response;
    };

    static getAttributeById = async(id:string) : Promise<any> => {
            const response = await Api.get(attribute + "/" +  id);
            return response;
    };

    static getAttributeByIdExtended = async(id:string) : Promise<any> => {
            const response = await Api.get(attribute + "/" +  id + extended);
            return response;
    }

    static addAttribute = async(newAttribute:AttributeDefinition) : Promise<any> => {
            const response = await Api.post(attribute, JSON.stringify(newAttribute));
            return response;
    }


    static updateAttributeById = async(id:string,attributeDTOExtended:AttributeDTOExtended) : Promise<any> => {
            const response = await Api.put(attribute + "/" + id, JSON.stringify(attributeDTOExtended));
            return response;
    }

    static deleteAttributeById = async(id:string) : Promise<any> => {
            const response = await Api.delete(attribute + "/" + id);
            return response;
    }

    static addAttributeValue = async(attributeId:string, attributeValue:AttributeValue) : Promise<any> => {
            const response = await Api.post(attribute + "/" + attributeId + attrValue,  JSON.stringify(attributeValue));
            return response;
    }

    static deleteAttributeValueById = async(attributeId:string, attributeValueId:string) : Promise<any> => {
            const response = await Api.delete(attribute + "/" + attributeId + attrValue + "/" + attributeValueId);
            return response;
    }
}




