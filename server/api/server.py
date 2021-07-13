from typing import Optional

from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from webParser import youtube

from ai import nltk_summary
from ai import dl_summary

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SummaryRequest(BaseModel):
    url: str
    textlen: float
    # language: str


class SummaryResponse(BaseModel):
    summary: Optional[str]
    error: Optional[str]
    detail: Optional[str]
    # language: str


class HealthResponse(BaseModel):
    status: float
    detail: str


class HealthRequest(BaseModel):
    check: Optional[str] = None


@app.get("/api/v1/health", response_model=HealthResponse)
async def health(request: HealthRequest):
    return HealthResponse(
        status=200,
        detail="API version 1 working",
    )


@app.get("/api/v1/summary", response_model=SummaryResponse)
async def summary(
    url: str = Query(
        ...,
        alias="url",
        title="Url of summary target",
        description="Url. ex: youtube url",
        deprecated=False,
    ),
    textlen: str = Query(
        150,
        alias="textlen",
        title="Maximum length of summary",
        description="Maximum length of the summary. Default is 150. ex: 150",
        deprecated=False,
    ),
):
    sub, error = youtube.youtube_sub(url)
    if error != None:
        return SummaryResponse(error="Error occured", detail=error)
    # print(f"recived from youtube => ", sub)

    # NOTE: nltk doesnt have control over textlength
    summaryText = nltk_summary.getSummary(sub, textlen)

    return SummaryResponse(
        summary=summaryText,
    )


@app.get("/api/v1/experimental/summary", response_model=SummaryResponse)
async def deepLearningSummary(
    url: str = Query(
        ...,
        alias="url",
        title="Url of summary target",
        description="Url. ex: youtube url",
        deprecated=False,
    ),
    textlen: str = Query(
        150,
        alias="textlen",
        title="Maximum length of summary",
        description="Maximum length of the summary. Default is 150. ex: 150",
        deprecated=False,
    ),
):

    sub, error = youtube.youtube_sub(request.url)
    if error != None:
        return SummaryResponse(error="Error occured", detail=error)
    textlength = 512 if int(request.textlen) > 512 else int(request.textlen)

    words = sub.count(" ") + 1
    textlength = textlength if textlength < words else words
    print(f"recived from youtube => ", sub)
    # NOTE: nltk doesnt have control over textlength
    summaryText = dl_summary.summary_t5_small(sub, textlength)

    return SummaryResponse(
        summary=summaryText,
    )
