import { Link, Outlet, useNavigate } from "react-router-dom";
import './ScanPage.css';
import { useContext, useState, useEffect } from "react";
import React, { Component } from 'react'
import { QrReader } from 'react-qr-reader';
import button from '../../assets/gobutton2.png'
import { BACKEND_URL, BACKEND_PATH_FOR_BENCH_DETAILS } from "../../default_values/constants";


// makes the reader component
// this is adapted from the examples from both https://www.npmjs.com/package/react-qr-scanner?activeTab=readme and 
// https://github.com/react-qr-reader/react-qr-reader on feb 20 2023
// it has been adapted to allow for storage of various album data and the rendering has been greatly changed


class Reader extends Component {
    constructor(props){
        super(props)
        this.state = {
            delay: 200,
            result: {text: ''},
            album: "An album name will appear here when you scan a QR code",
            author: "An author will appear here when you scan a QR code",
            img: "/default_album_art.svg",
            url: "",
        }
        this.setData = this.setData.bind(this)
        this.handleError = this.handleError.bind(this)
        this.getInfo = this.getInfo.bind(this)
    }

    getInfo(){  
        // edit this later
        fetch(`${BACKEND_URL}${BACKEND_PATH_FOR_BENCH_DETAILS}${this.state.url}/`, {
            method: 'GET',
        }).then(res => {
            if (res.status === 404) {
                navigate('/');
            }
            return res.json()
        }).then(data => {
            console.log(data);
            setTitle(data.bench_title);
            setAuthor(data.audio_details.contributor);
            setAlbumArt(`${BACKEND_URL}${data.thumbnail}`);
        }).catch(err => {
            console.log(err);
            console.log("error");
        });
    }

    // this is what the reader will do when the camera is on and it is trying to scan
    // continuously scans null if there is no qr code
    setData(data){ 
        if(data){
            this.setState({
                result: data,
                album: data.text.split("=")[1],
                author: data.text.split("=")[1],
                img: data.text.split("=")[1],
                url: data,
            })
        }
      
        if (this.state.result != null){   // when qr code is found, it will do something
            console.log(this.state.result)
        }
    }

    

    // error handling
    handleError(err){
        // console.error(err)
    }

    // renders the scanner 
    render(){
        return(
            <div className="scan-page-wrapper">
            <QrReader className="scanner"
                onResult={(result, error) => {
                    if (!!result) {
                      this.setData(result);
                    }
                    if (!!error) {
                      this.handleError(error);
                    }
                  }}

                  constraints={{
                            facingMode: "environment"
                    }}
                />
                <div className="album-info">
                <img className="scan-album-art" src={process.env.PUBLIC_URL + this.state.img} alt='' />
                    <div className="album-txt">
                        <p className="album">Album: {this.state.album}</p>
                        <p className="author">Author: {this.state.author}</p>
                    </div>
                </div>
                <Link to={this.state.url}>
                    <img className="redirect-button" src={button} alt="" />
                </Link>
            </div>
        )
    }
}

// scanpage render
const ScanPage = () => {
    return (
        <>
            <nav className="scan-page">
                <h1>Take Camera over a QR code at any of our parks</h1>
                <Reader> </Reader>
            </nav>
            <Outlet />
        </>
    )
}

export default ScanPage;