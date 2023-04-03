import { tone1, tone2 } from "../defaults";

const PlayButton = (props) => {
    return (
        <>
            <svg width="75" height="75" viewBox="0 0 75 75" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="37.5" cy="37.5" r="37.5" fill={props.tone1 || tone1} />
                <path d="M29.25 23.2106L54 37.5L29.25 51.7894L29.25 23.2106Z" fill={props.tone1 || tone1} stroke={props.tone2 || tone2} strokeWidth="6" />
            </svg>
        </>
    )
}
export default PlayButton;