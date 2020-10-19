import {backendLookup} from '../lookup'


export function apiBoardCreate(newBoardName, callback){
    backendLookup("POST", "/", callback, {name:newBoardName})
}

export function apiBoardsList(callback){
    backendLookup("GET", "/", callback)
}

export function apiBoardDetails(boardId, callback){
    backendLookup("GET", `/${boardId}`, callback)
}

export function apiStickerCreate(newStickerTitle, newStickerBoard, newStickerContent, newStickerAlert, callback){
    backendLookup(
        "POST", 
        "/stickers/sticker/create", 
        callback, 
        {title:newStickerTitle, board:newStickerBoard, content: newStickerContent, alert_time: newStickerAlert}
    )
}

export function apiStickersList(callback){
    backendLookup("GET", "/stickers/", callback)
}

export function apiStickerDetails(stickerId, callback){
    backendLookup("GET", `/stickers/${stickerId}`, callback)
}