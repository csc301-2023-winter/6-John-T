import { Outlet, useNavigate, useSearchParams } from "react-router-dom";
import './MediaPage.css';
import { useState, useEffect } from "react";
import default_album_art from '../../assets/default_album_art.svg';
import PlayButton from "./media_buttons/PlayButton";
import PauseButton from "./media_buttons/PauseButton";
import ForwardButton from "./media_buttons/ForwardButton";
import RewindButton from "./media_buttons/RewindButton";
import { BACKEND_URL, BACKEND_PATH_FOR_BENCH_DETAILS } from "../../default_values/constants";

// custom hook for audio
// this hook is adapted from https://stackoverflow.com/a/47686478 on feb 20 2023
// i have changed it to add skip functionality and added a few event listeners
const useAudio = url => {
    const [audio, setAudio] = useState(new Audio(url));
    const [playing, setPlaying] = useState(false);
    const toggle = () => setPlaying(!playing);

    const skip = (time) => {
        if (time === 'back') {
            audio.currentTime = audio.currentTime - 10;
        } else if (time === 'fwd') {
            audio.currentTime = audio.currentTime + 10;
        }
    };

    useEffect(() => {
        playing ? audio.play() : audio.pause();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [playing]);

    useEffect(() => {
        audio.addEventListener('ended', () => setPlaying(false));
        audio.addEventListener('play', () => setPlaying(true));
        audio.addEventListener('pause', () => setPlaying(false));
        return () => {
            audio.removeEventListener('ended', () => setPlaying(false));
        };
    }, [audio]);

    return [playing, toggle, skip, setAudio];
};


const MediaPage = () => {
    const [searchParams] = useSearchParams();
    const [title, setTitle] = useState("Mindfulness at Charleston Lake");
    const [author, setAuthor] = useState("Paula Vital");
    const [playing, toggle, skip, setAudio] = useAudio(null);
    const [loading, setLoading] = useState(true);

    const navigate = useNavigate();
    const [hasAudio, setHasAudio] = useState(false);
    const [album_art, setAlbumArt] = useState(null);

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
            // fetch the media from the backend
            fetch(`${BACKEND_URL}${BACKEND_PATH_FOR_BENCH_DETAILS}${x}/`, {
                method: 'GET',
            }).then(res => {
                if (res.status === 404) {
                    navigate('/');
                }
                return res.json()
            }).then(data => {
                console.log(data);
                setTitle(data.bench_title);
                if (data.thumbnail !== '') {
                    setAlbumArt(`${BACKEND_URL}${data.thumbnail}`);
                }
                if (data.audio_details.audio_binary) {
                    setAuthor(data.audio_details.contributor);
                    setHasAudio(true);
                    fetch(`${BACKEND_URL}${data.audio_details.audio_file}`).then(r => r.blob()).then(blob => {
                        const aud = new Audio(URL.createObjectURL(blob));
                        setAudio(aud);
                        setLoading(false);
                    });
                }
            }).catch(err => {
                console.log(err);
                console.log("error");
            });

        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
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
                {hasAudio ? (loading ? <div className="mediapage-loader"></div> :
                    <div className="media-buttons">
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
                    </div>) :
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