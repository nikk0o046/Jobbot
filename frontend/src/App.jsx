import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NavBar from './components/NavBar';
import ProfilePage from './pages/ProfilePage';
import SwipingPage from './pages/SwipingPage';
import LikesPage from './pages/LikesPage';
import AppProvider from './AppProvider';

function App() {
    return (
      <AppProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/profile" element={<ProfilePage />} />
            <Route path="/swiping" element={<SwipingPage />} />
            <Route path="/likes" element={<LikesPage />} />
            <Route path="/" element={<ProfilePage />} /> {/* Default page */}
          </Routes>
          <NavBar />
        </BrowserRouter>
      </AppProvider>
    );
}  

export default App;

