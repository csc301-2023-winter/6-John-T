import { Link, Outlet, useNavigate } from "react-router-dom";
import './ScanPage.css';
import { useContext, useState, useEffect } from "react";
import React, { Component } from 'react'
import QrReader from 'react-qr-scanner'
import button from '../../assets/gobutton2.png'
import clake from '../../assets/clake.png'

// makes the reader component
// this is adapted from the example from https://www.npmjs.com/package/react-qr-scanner?activeTab=readme on feb 20 2023
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
            url: ""
        }
        this.handleScan = this.handleScan.bind(this)
        this.handleError = this.handleError.bind(this)
    }

    //this is what the reader will do when the camera is on and it is trying to scan
    //continuously scans null if there is no qr code
    handleScan(data){ 
        if(data){
            this.setState({
                result: data,
                album: data.text.split("|")[0],
                author: data.text.split("|")[1],
                img: data.text.split("|")[2],
                url: data.text.split("|")[3],
            })
        }
      
      /*
        if (this.state.result != null){   //when qr code is found, it will do something
        console.log(this.state.result)
      }
      */
    }

    //error handling
    handleError(err){
        console.error(err)
    }

    //renders the scanner 
    render(){
        return(
            <div className="scan-page-wrapper">
            <QrReader className="scanner"
                delay={this.state.delay}
                onError={this.handleError}
                onScan={this.handleScan}
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