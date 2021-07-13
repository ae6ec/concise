import axios, { AxiosResponse } from 'axios';

import React, { useState, useEffect } from 'react';
import logo from './assets/logo192.png';
import './App.css';

import { SummaryRequest,SummaryResponse } from "./types";
import { EHC_SUMMARY_API } from "./config/api" 


/* TODO: add EHC api version in config and locastorage.
 * if changed than update the localstorage
*/



function App() {
  const [currentUrl, setCurrentUrl] = useState<string>('');
  const [responseFromContent, setResponseFromContent] = useState<string>('');
  
  /**
   * Get current URL
   */
  useEffect(() => {
      const queryInfo = {active: true, lastFocusedWindow: true};

      chrome.tabs && chrome.tabs.query(queryInfo, tabs => {
          const currentUrl = tabs[0].url;
          if(currentUrl !== undefined){
            setCurrentUrl(currentUrl);
          }
      });

  }, []);

  /*
  * Fetch summary if present in localstorage
  */
  
  useEffect(() => {
      const ytCode: string | null = getytCode(currentUrl);
      if (ytCode !== null) {
        const pageID: string = "youtube-" + ytCode
    
        chrome.storage.local.get([pageID], function(data) {
            if (typeof data[pageID] !== 'undefined')
              // console.log("Setting summary from storage")
              setResponseFromContent(data[pageID]);
          });
      } 
      // else console.log("No summary present in storage") 
    
  }, [currentUrl])

  function getytCode(url: string){
    let regExp = /^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
    let match = url.match(regExp);
    if (match && match[2].length == 11) {
      return match[2];
    } else {
      return null;
    }
  }
  
  function getAndSetSummary(){
    const ytCode: string | null = getytCode(currentUrl);
    
    if( ytCode === null){
      setResponseFromContent("Only youtube supported")
      return;
    }
    // TODO: fetch domain
    // hardcoding yt
    // const pageID: string = window.location.hostname + "-" + ytCode
    
    const pageID: string = "youtube-" + ytCode
    
    chrome.storage.local.get([pageID], async (data) =>  {
        if (typeof data[pageID].summary !== 'undefined'){
          // console.log("Setting summary from storage")
          setResponseFromContent(data[pageID]);
        }
        else{
            const summary: SummaryResponse = await getSummary();

            if(summary.summary !== null ) {
              setResponseFromContent(summary.summary)
              chrome.storage.local.set({ [pageID]: summary.summary}, () => {
                // console.log('Summary cached ' + summary.summary);
              });
            }
            else setResponseFromContent("Error occured. Make sure english subtitle present")
            
        }
      });
  }

  async function getSummary() {
    let summaryData: SummaryRequest = {
        url: currentUrl,
        textlen: 150
    }
    let data: SummaryResponse;
    try {
        const res: AxiosResponse = await axios.get(EHC_SUMMARY_API,{ 
            params: summaryData
        });
       data = res.data;
        
    } catch (error) {
      if (axios.isAxiosError(error)) {
          data = {
              summary: null,
              error: "Axios Error",
              detail: "Axios Error"
          }
        // console.log("Calling EHC summary, Axios error: ",{error});
      } else {
        data = {
            summary: null,
            error: "Error",
            detail: "Error"
        }
        // console.log("Calling EHC summary, Error occured at: ",{error});
      }
    }
    return data;
  }



  /**
   * Send message to the content script
   */
  // const sendSummaryMessage = async () => {
  //   // const queryInfo: chrome.tabs.QueryInfo = {
  //   //     active: true,
  //   //     currentWindow: true
  //   // };

  //   /**
  //    * We can't use "chrome.runtime.sendMessage" for sending messages from React.
  //    * For sending messages from React we need to specify which tab to send it to.
  //    */
  //   // chrome.tabs && chrome.tabs.query(queryInfo, tabs => {
  //   //     const currentTabId = tabs[0].id;
  //   //     /**
  //   //      * Sends a single message to the content script(s) in the specified tab,
  //   //      * with an optional callback to run when a response is sent back.
  //   //      *
  //   //      * The runtime.onMessage event is fired in each content script running
  //   //      * in the specified tab for the current extension.
  //   //      */
  //   //     if (currentTabId !== undefined){
  //   //         chrome.tabs.sendMessage(
  //   //             currentTabId,
  //   //             message,
  //   //             (response) => {
  //   //                 console.log(`response recieved from content.ts : ${JSON.parse(response)}`)
  //   //                 setResponseFromContent(response);
  //   //             });
  //   //     }else {
  //   //         console.log('Recieved undefined at currentTabId');
  //   //     }
  //   //     });
  //   // const summary: SummaryResponse = await getSummary();
  //   getAndSetSummary()
  //   console.log("data received ",{summary})
  //   if(summary.summary !== null ){
  //       setResponseFromContent(summary.summary)
  //   }
  //   else setResponseFromContent("Error occured. Make sure english subtitile present")
  // };

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo"/>
                <div className="app-header-text">
                  Concise
              </div>
            </header>
            <button onClick={getAndSetSummary}>Summary</button>
            <p>Summary: </p>
            <p>{responseFromContent}</p>
        </div>
    );
};

export default App;