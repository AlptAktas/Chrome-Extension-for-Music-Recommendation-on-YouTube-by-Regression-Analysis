var port = chrome.runtime.connect({
    name: 'Communication with background.js',
});


port.postMessage("Post Message to Background");
port.onMessage.addListener(function(response) {
    if(response == "done"){
        chrome.storage.sync.get(null, function(data) {
            //document.getElementById("link_2").innerHTML = data.link_2;
            document.getElementById("name_1").innerHTML = data.name_1;
            document.getElementById("name_2").innerHTML = data.name_2;
            document.getElementById("name_3").innerHTML = data.name_3;
            document.getElementById("name_4").innerHTML = data.name_4;
            document.getElementById("name_5").innerHTML = data.name_5;
            document.getElementById("link_1").setAttribute("src",data.link_1);
            document.getElementById("link_2").setAttribute("src",data.link_2);
            document.getElementById("link_3").setAttribute("src",data.link_3);
            document.getElementById("link_4").setAttribute("src",data.link_4);
            document.getElementById("link_5").setAttribute("src",data.link_5);
        });
    }
    else if(response == "empty"){
        console.log('empty')
    }
    else{
        console.log('full')
        chrome.storage.sync.get(null, function(data) {
            document.getElementById("name_1").innerHTML = data.name_1;
            document.getElementById("name_2").innerHTML = data.name_2;
            document.getElementById("name_3").innerHTML = data.name_3;
            document.getElementById("name_4").innerHTML = data.name_4;
            document.getElementById("name_5").innerHTML = data.name_5;
            document.getElementById("link_1").setAttribute("src",data.link_1);
            document.getElementById("link_2").setAttribute("src",data.link_2);
            document.getElementById("link_3").setAttribute("src",data.link_3);
            document.getElementById("link_4").setAttribute("src",data.link_4);
            document.getElementById("link_5").setAttribute("src",data.link_5);
        });
    }

});
/*
chrome.runtime.sendMessage({} ,(response) => {
            music_url = response.url;
            for(var key in music_url){
                if(music_url.hasOwnProperty(key)){
                    console.log(key + "-->" + music_url[key]);
                    document.getElementById("link_1").innerHTML = music_url[key]
                }
            }
        });

*/


/*
chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        if(tabs.length == 0){}
        console.log(tabs[0].url);
        fetch("http://127.0.0.1:8000/api?url=" + tabs[0].url).then(response => response.json()).then(result => {
            for(var key in result){
                if(result.hasOwnProperty(key)){
                    console.log(key + "-->" + result[key]);
                    document.getElementById("link_1").innerHTML = result[key]
                }
            }
        });

});
*/


/*
fetch("http://127.0.0.1:8000/api" + "?url=https://www.youtube.com/watch?v=Dn0JPuwvJgY")
    .then(response => response.json())
    .then(result => {
        console.log(result);
        //document.getElementById("link_1").innerHTML = result
    })
    */