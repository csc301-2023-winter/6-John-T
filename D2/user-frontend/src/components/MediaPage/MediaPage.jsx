import { Outlet, useNavigate, useSearchParams } from "react-router-dom";
import './MediaPage.css';
import { useState, useEffect } from "react";
import album_art from '../../assets/mock_data/album_art.png';
import default_album_art from '../../assets/default_album_art.svg';
import PlayButton from "./media_buttons/PlayButton";
import PauseButton from "./media_buttons/PauseButton";
import ForwardButton from "./media_buttons/ForwardButton";
import RewindButton from "./media_buttons/RewindButton";
import mock_audio from '../../assets/mock_data/mock_audio.mp3';

// custom hook for audio
// this hook is adapted from https://stackoverflow.com/a/47686478 on feb 20 2023
// i have changed it to add skip functionality and added a few event listeners
const useAudio = url => {
    const [audio] = useState(new Audio(url));
    const [playing, setPlaying] = useState(false);

    const toggle = () => setPlaying(!playing);

    const skip = (time) => {
        if (time == 'back') {
            audio.currentTime = audio.currentTime - 10;
        } else if (time == 'fwd') {
            audio.currentTime = audio.currentTime + 10;
        }
    };

    useEffect(() => {
        playing ? audio.play() : audio.pause();
    }, [playing]);

    useEffect(() => {
        audio.addEventListener('ended', () => setPlaying(false));
        audio.addEventListener('play', () => setPlaying(true));
        audio.addEventListener('pause', () => setPlaying(false));
        return () => {
            audio.removeEventListener('ended', () => setPlaying(false));
        };
    }, []);

    return [playing, toggle, skip];
};


const MediaPage = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [title, setTitle] = useState("Mindfulness At Charleston Lake");
    const [author, setAuthor] = useState("Paula Vital");
    const [playing, toggle, skip] = useAudio(mock_audio);
    const navigate = useNavigate();

    // color scheme
    const tone1 = "#C4B59B";
    const tone2 = "#241F21";

    // check if media query is provided in the url
    useEffect(() => {
        let x = searchParams.get('m');
        if (x === null) {
            navigate('/');
        }
        else {
            console.log("x is not null");
        }
    }, []);

    // pauses the song
    const pauseHandler = () => {
        console.log("pause handler");
        toggle();
    };

    // plays the song
    const playHandler = () => {
        console.log("play handler");
        toggle();
    };

    // forwards the song by 10 seconds
    const forwardHandler = () => {
        console.log("forward handler");
        skip('fwd');
    };

    // rewinds the song by 10 seconds
    const rewindHandler = () => {
        console.log("rewind handler");
        skip('back');
    };


    return (
        <>
            <div className="media-page">
                <img src={album_art || default_album_art} alt="" className="album-art" />
                <p className="album-title">{title}</p>
                <p className="album-author">{author || ''}</p>
                {mock_audio
                    ? <div className="media-buttons">
                        <div onClick={() => rewindHandler()}>
                            <RewindButton tone1={tone1} tone2={tone2} />
                        </div>
                        {playing ?
                            <div onClick={() => pauseHandler()}>
                                <PauseButton tone1={tone1} tone2={tone2} />
                            </div>
                            :
                            <div onClick={() => playHandler()}>
                                <PlayButton tone1={tone1} tone2={tone2} />
                            </div>
                        }
                        <div onClick={() => forwardHandler()}>
                            <ForwardButton tone1={tone1} tone2={tone2} />
                        </div>
                    </div> :
                    <div className="no-audio-sign">
                        <p>No audio available</p>
                    </div>
                }
            </div>
            <Outlet />
        </>
    )
}

export default MediaPage;