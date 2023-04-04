import { tone1, tone2 } from "../defaults";

const RewindButton = (props) => {
    return (
        <>
            <svg width="55" height="55" viewBox="0 0 55 55" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="27.5" cy="27.5" r="27.5" transform="matrix(-1 0 0 1 55 0)" fill={props.tone1 || tone1} />
                <mask id="path-2-inside-1_5_50" fill="white">
                    <path d="M15.3736 37.3647C17.2403 39.8693 19.858 41.7125 22.8452 42.6258C25.8324 43.5391 29.0333 43.4748 31.9814 42.4422C34.9295 41.4097 37.471 39.4628 39.2356 36.8853C41.0002 34.3077 41.8958 31.2341 41.7919 28.1121C41.688 24.9901 40.59 21.9828 38.6579 19.5283C36.7258 17.0738 34.0605 15.3002 31.0502 14.466C28.0399 13.6318 24.8419 13.7805 21.922 14.8904C19.0021 16.0003 16.5128 18.0135 14.8168 20.6367L27.1333 28.6L15.3736 37.3647Z" />
                </mask>
                <path d="M15.3736 37.3647C17.2403 39.8693 19.858 41.7125 22.8452 42.6258C25.8324 43.5391 29.0333 43.4748 31.9814 42.4422C34.9295 41.4097 37.471 39.4628 39.2356 36.8853C41.0002 34.3077 41.8958 31.2341 41.7919 28.1121C41.688 24.9901 40.59 21.9828 38.6579 19.5283C36.7258 17.0738 34.0605 15.3002 31.0502 14.466C28.0399 13.6318 24.8419 13.7805 21.922 14.8904C19.0021 16.0003 16.5128 18.0135 14.8168 20.6367L27.1333 28.6L15.3736 37.3647Z" fill="#D9D9D9" stroke={props.tone2 || tone2} strokeWidth="12" mask="url(#path-2-inside-1_5_50)" />
                <circle cx="11.4667" cy="11.4667" r="11.4667" transform="matrix(-1 0 0 1 38.6 17.1335)" fill={props.tone1 || tone1} />
                <path d="M12.3077 25.814L23.4666 23.1L13.9333 14.3L12.3077 25.814Z" fill={props.tone2 || tone2} />
                <path d="M22.5573 25.7273V33H21.0196V27.1868H20.977L19.3115 28.2308V26.8672L21.1119 25.7273H22.5573ZM27.1373 33.1598C26.5265 33.1574 26.001 33.0071 25.5606 32.7088C25.1227 32.4105 24.7853 31.9785 24.5486 31.4126C24.3142 30.8468 24.1982 30.1662 24.2006 29.3707C24.2006 28.5777 24.3177 27.9018 24.5521 27.343C24.7889 26.7843 25.1262 26.3594 25.5642 26.0682C26.0045 25.7746 26.5289 25.6278 27.1373 25.6278C27.7458 25.6278 28.269 25.7746 28.7069 26.0682C29.1473 26.3617 29.4858 26.7879 29.7226 27.3466C29.9593 27.9029 30.0765 28.5777 30.0741 29.3707C30.0741 30.1686 29.9558 30.8504 29.719 31.4162C29.4846 31.982 29.1485 32.4141 28.7105 32.7124C28.2725 33.0107 27.7481 33.1598 27.1373 33.1598ZM27.1373 31.8849C27.554 31.8849 27.8866 31.6754 28.1352 31.2564C28.3838 30.8374 28.5069 30.2088 28.5045 29.3707C28.5045 28.8191 28.4477 28.3598 28.3341 27.9929C28.2228 27.6259 28.0642 27.3501 27.8582 27.1655C27.6546 26.9808 27.4143 26.8885 27.1373 26.8885C26.723 26.8885 26.3916 27.0956 26.143 27.5099C25.8944 27.9242 25.769 28.5445 25.7666 29.3707C25.7666 29.9295 25.8222 30.3958 25.9335 30.7699C26.0471 31.1416 26.2069 31.4209 26.4129 31.608C26.6189 31.7926 26.8604 31.8849 27.1373 31.8849ZM35.7231 29.1009L34.3382 29.1861C34.3145 29.0677 34.2636 28.9612 34.1855 28.8665C34.1073 28.7694 34.0044 28.6925 33.8765 28.6357C33.751 28.5765 33.6007 28.5469 33.4255 28.5469C33.1911 28.5469 32.9935 28.5966 32.8325 28.696C32.6715 28.7931 32.591 28.9233 32.591 29.0866C32.591 29.2169 32.6431 29.3269 32.7472 29.4169C32.8514 29.5069 33.0302 29.5791 33.2835 29.6335L34.2707 29.8324C34.801 29.9413 35.1963 30.1165 35.4568 30.358C35.7172 30.5994 35.8474 30.9167 35.8474 31.3097C35.8474 31.6671 35.742 31.9808 35.5313 32.2507C35.323 32.5206 35.0365 32.7313 34.672 32.8828C34.3097 33.032 33.8919 33.1065 33.4184 33.1065C32.6963 33.1065 32.1211 32.9562 31.6926 32.6555C31.2664 32.3525 31.0167 31.9406 30.9433 31.4197L32.4312 31.3416C32.4762 31.5618 32.5851 31.7299 32.7579 31.8459C32.9307 31.9595 33.1521 32.0163 33.422 32.0163C33.6871 32.0163 33.9002 31.9654 34.0612 31.8636C34.2245 31.7595 34.3074 31.6257 34.3097 31.4624C34.3074 31.325 34.2494 31.2126 34.1357 31.125C34.0221 31.035 33.8469 30.9664 33.6102 30.919L32.6656 30.7308C32.1329 30.6243 31.7364 30.4396 31.4759 30.1768C31.2179 29.9141 31.0889 29.5791 31.0889 29.1719C31.0889 28.8215 31.1836 28.5196 31.373 28.2663C31.5647 28.013 31.8334 27.8177 32.1791 27.6804C32.5271 27.5431 32.9343 27.4744 33.4007 27.4744C34.0896 27.4744 34.6317 27.62 35.0271 27.9112C35.4248 28.2024 35.6568 28.599 35.7231 29.1009Z" fill={props.tone2 || tone2} />
            </svg>

        </>
    )
}

export default RewindButton;