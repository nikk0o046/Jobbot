import { useState, useContext } from 'react';
import { AppContext } from '../AppProvider';
import { Box, IconButton, Typography } from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';
import CloseIcon from '@mui/icons-material/Close';
import StarIcon from '@mui/icons-material/Star';

function SwipingPage() {
  const { jobSummaries, setJobSummaries, likes, setLikes, superlikes, setSuperlikes, userHasSubmitted } = useContext(AppContext);

  const handleLike = () => {
    if (jobSummaries.length > 0) {
      setLikes([...likes, jobSummaries[0]]);
      setJobSummaries(jobSummaries.slice(1));
    }
  };

  const handleDislike = () => {
    if (jobSummaries.length > 0) {
      setJobSummaries(jobSummaries.slice(1));
    }
  };

  const handleSuperLike = () => {
    if (jobSummaries.length > 0) {
      setSuperlikes([...superlikes, jobSummaries[0]]);
      setJobSummaries(jobSummaries.slice(1));
    }
  };

  return (
    <Box sx={{ m: 2 }}>
      {userHasSubmitted ? (
        jobSummaries && jobSummaries.length > 0 ? (
          <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Typography variant="body1" sx={{ my: 2 }}>
              {jobSummaries[0]}
            </Typography>
            <Box sx={{ display: 'flex', justifyContent: 'space-around', width: '100%' }}>
              <IconButton color="error" onClick={handleDislike}>
                <CloseIcon fontSize="large" />
              </IconButton>
              <IconButton color="primary" onClick={handleSuperLike}>
                <StarIcon />
              </IconButton>
              <IconButton color="success" onClick={handleLike}>
                <FavoriteIcon fontSize="large" />
              </IconButton>
            </Box>
          </Box>
        ) : (
          <Typography>There are no more jobs available.</Typography>
        )
      ) : (
        <Typography>You have to complete your profile before swiping!</Typography>
      )}
    </Box>
  );
}

export default SwipingPage;

