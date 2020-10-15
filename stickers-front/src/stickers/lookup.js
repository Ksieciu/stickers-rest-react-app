import {backendLookup} from '../lookup'

export function apiStickerCreate(newStickerTitle, newStickerContent, newStickerAlert, callback){
    backendLookup("POST", "/stickers/", callback, {title:newStickerTitle, content: newStickerContent, alert_time: newStickerAlert})
}

export function apiStickerList(callback){
    backendLookup("GET", "/stickers/", callback)
}