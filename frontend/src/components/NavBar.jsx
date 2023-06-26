import React from 'react';
import { useLocation, Link } from 'react-router-dom';
import { BottomNavigation, BottomNavigationAction } from '@mui/material';
import ProfileIcon from '@mui/icons-material/Person'; // For "Profile" page
import SwipingIcon from '@mui/icons-material/SwapHorizontalCircle'; // For "Swiping" page
import LikesIcon from '@mui/icons-material/Favorite'; // For "Likes" page

function NavBar() {
    const location = useLocation();
  
    return (
      <BottomNavigation 
        showLabels 
        value={location.pathname}
        style={{ width: '100%', position: 'fixed', bottom: 0 }}
      >
        <BottomNavigationAction
          label="Profile"
          value="/profile"
          icon={<ProfileIcon />}
          component={Link}
          to="/profile"
        />
        <BottomNavigationAction
          label="Swiping"
          value="/swiping"
          icon={<SwipingIcon />}
          component={Link}
          to="/swiping"
        />
        <BottomNavigationAction
          label="Likes"
          value="/likes"
          icon={<LikesIcon />}
          component={Link}
          to="/likes"
        />
      </BottomNavigation>
    );
  }  

export default NavBar;
