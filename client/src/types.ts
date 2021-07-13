
export enum Sender {
    React,
    Content
}

export interface ChromeMessage {
    from: Sender,
    message: any
}

export interface SummaryRequest{
    url: string,
    textlen: Number    
}

export interface SummaryResponse{
    summary: string | null,
    error: string | null,
    detail: string | null    
}