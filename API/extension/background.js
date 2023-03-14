chrome.storage.sync.set({'name_1': ''})
chrome.storage.sync.set({'name_2': ''})
chrome.storage.sync.set({'name_3': ''})
chrome.storage.sync.set({'name_4': ''})
chrome.storage.sync.set({'name_5': ''})
chrome.storage.sync.set({'link_1': ''})
chrome.storage.sync.set({'link_2': ''})
chrome.storage.sync.set({'link_3': ''})
chrome.storage.sync.set({'link_4': ''})
chrome.storage.sync.set({'link_5': ''})
chrome.storage.sync.set({'url': ''})

var base_url = "https://www.youtube.com/embed/"

chrome.runtime.onConnect.addListener((port) => {
    console.log("Connected...");
    port.onMessage.addListener((response) => {
        chrome.storage.sync.get(['link_1', 'url'], (data) => {
            chrome.tabs.query({active: true, lastFocusedWindow: true}, (tabs) => {
                y_url = tabs[0].url;
                console.log(y_url);
                if(y_url.length == 0){
                    port.postMessage("empty");
                    return true;
                }
                if(data.url == y_url){
                    port.postMessage("full");
                    return true;
                }
                if(data.url != y_url){
                    fetch("http://127.0.0.1:8000/api?url=" + y_url).then(response => response.json()).then(result => {
                        for(var key in result){
                            if(result.hasOwnProperty(key)){
                                console.log(key + "-->" + result[key]);
                            }
                        }
                        chrome.storage.sync.set({'name_1': result[0].artist_name + " - " + result[0].track_name})
                        chrome.storage.sync.set({'name_2': result[1].artist_name + " - " + result[1].track_name})
                        chrome.storage.sync.set({'name_3': result[2].artist_name + " - " + result[2].track_name})
                        chrome.storage.sync.set({'name_4': result[3].artist_name + " - " + result[3].track_name})
                        chrome.storage.sync.set({'name_5': result[4].artist_name + " - " + result[4].track_name})
                        chrome.storage.sync.set({'link_1': base_url + result[0].youtube_url})
                        chrome.storage.sync.set({'link_2': base_url + result[1].youtube_url})
                        chrome.storage.sync.set({'link_3': base_url + result[2].youtube_url})
                        chrome.storage.sync.set({'link_4': base_url + result[3].youtube_url})
                        chrome.storage.sync.set({'link_5': base_url + result[4].youtube_url})
                        chrome.storage.sync.set({'url': y_url})
                        port.postMessage("done");
                    });
                    return true;
                }
            });
        });
    });
});

/*
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    var tab_url = "";
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        if(tabs.length == 0){
            sendResponse({});
            return false;
        }
        console.log(tabs[0].url);
        fetch("http://127.0.0.1:8000/api?url=" + tabs[0].url).then(response => response.json()).then(result => {
            for(var key in result){
                if(result.hasOwnProperty(key)){
                    console.log(key + "-->" + result[key]);
                }
            }
        sendResponse({url: result});
        });

    });
    return true;
});

*/