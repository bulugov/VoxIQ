import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './VoxIQ.css';

function VoxIQ() {
    const [isRecording, setIsRecording] = useState(false);
    const [dropdownOpen, setDropdownOpen] = useState(false);

    const toggleRecording = () => {
        setIsRecording(!isRecording);
    };

    const toggleDropdown = () => {
        setDropdownOpen(!dropdownOpen);
    };

    return (
        <div className="voxiq-container">
            <div className="top-right-text">
                <div>About Us</div>
                <div>Help</div>
            </div>
            <div className="dropdown">
                <button onClick={toggleDropdown} className="dropbtn">Menu</button>
                {dropdownOpen && (
                    <div className="dropdown-content">
                        <Link to="/" onClick={() => setDropdownOpen(false)}>Home</Link>
                        <Link to="/quotes" onClick={() => setDropdownOpen(false)}>Quotes</Link>
                    </div>
                )}
            </div>
            <h1>VoxIQ</h1>
            <button onClick={toggleRecording}>
                {isRecording ? 'Stop Recording' : 'Record Audio'}
            </button>
            <div className="footer-text">
                Canadian University Dubai
            </div>
        </div>
    );
}

export default VoxIQ;



