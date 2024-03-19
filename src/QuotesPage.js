import React from 'react';
import './QuotesPage.css';

function QuotesPage() {
    return (
        <div className="quotes-container">
            <h1>Quotes</h1>
            <button className="search-button">Search Quotes</button>
            <div className="quote">The only way to do great work is to love what you do.</div>
            <div className="quote">It does not matter how slowly you go as long as you do not stop.</div>
            <div className="quote">Success is not final, failure is not fatal: It is the courage to continue that counts.</div>
        </div>
    );
}

export default QuotesPage;


