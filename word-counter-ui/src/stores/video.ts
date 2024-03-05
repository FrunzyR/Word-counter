import { defineStore } from "pinia"
import { ref, computed } from "vue"

function youtube_parser(url: string): string{
    if(!url) return " ";

    var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
    var match = url.match(regExp);
    return (match&&match[7].length==11)? match[7] : "";
}

export const useVideoStore = defineStore('video', () => {

    //state
    const videoURL = ref("")
    const videoId = computed(() => youtube_parser(videoURL.value))

    //mutations
    function changeVideoURL(newVideoURL: string){
        videoURL.value = newVideoURL
    }

    return {videoId, videoURL, changeVideoURL}
})

