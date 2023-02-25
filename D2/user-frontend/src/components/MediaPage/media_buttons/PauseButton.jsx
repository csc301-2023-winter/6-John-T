import { tone1, tone2 } from "../defaults";

const PauseButton = (props) => {
    return (
        <>
            <svg width="75" height="75" viewBox="0 0 75 75" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="37.5" cy="37.5" r="37.5" fill={props.tone1 || tone1} />
                <rect x="24" y="20" width="8" height="36" fill={props.tone2 || tone2} />
                <rect x="43" y="20" width="8" height="36" fill={props.tone2 || tone2} />
            </svg>
        </>
    )
}

export default PauseButton;