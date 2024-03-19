import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import VoxIQ from './VoxIQ'; 
import QuotesPage from './QuotesPage'; 

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/Quotes" element={<QuotesPage />} />
          <Route path="/" element={<VoxIQ />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

