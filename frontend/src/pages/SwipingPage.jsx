import { useState, useContext } from 'react';
import { AppContext } from '../AppProvider'; // Import the AppContext
import { Box, IconButton, Typography } from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';
import CloseIcon from '@mui/icons-material/Close';
import StarIcon from '@mui/icons-material/Star';

function SwipingPage() {
  const { jobSummaries, setJobSummaries } = useContext(AppContext); // Use the context

  const handleButtonClick = () => {
    setJobSummaries(jobSummaries.slice(1));
  };

  return (
    <Box sx={{ m: 2 }}> {/* Added some margin */}
      <Typography variant="h4">Job Swipe Page</Typography>
      {jobSummaries && jobSummaries.length > 0 ? ( // Check if jobSummaries exist and are not empty
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <Typography variant="body1" sx={{ my: 2 }}>
            {jobSummaries[0]} {/* Show the first job in the list */}
          </Typography>
          <Box sx={{ display: 'flex', justifyContent: 'space-around', width: '100%' }}>
            <IconButton color="error" onClick={handleButtonClick}>
              <CloseIcon fontSize="large" />
            </IconButton>
            <IconButton color="primary" onClick={handleButtonClick}>
              <StarIcon />
            </IconButton>
            <IconButton color="success" onClick={handleButtonClick}>
              <FavoriteIcon fontSize="large" />
            </IconButton>
          </Box>
        </Box>
      ) : (
        <Typography>You have to complete your profile before swiping!</Typography>
      )}
    </Box>
  );
}

export default SwipingPage;
