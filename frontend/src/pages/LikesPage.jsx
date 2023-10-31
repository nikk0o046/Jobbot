import React, { useContext, useState } from 'react';
import { AppContext } from '../AppProvider'; // Import the AppContext
import { 
  Box, 
  Typography, 
  Table, 
  TableBody, 
  TableCell, 
  TableContainer, 
  TableHead, 
  TableRow, 
  Paper,
  Dialog, 
  DialogActions, 
  DialogContent, 
  DialogContentText, 
  DialogTitle, 
  Button 
} from '@mui/material';

function LikesPage() {
  // Context to get superlikes and likes
  const { superlikes, likes } = useContext(AppContext); 

  // State to control Dialog visibility
  const [open, setOpen] = useState(false);

  // Open the Dialog
  const handleClickOpen = () => {
    setOpen(true);
  };

  // Close the Dialog
  const handleClose = () => {
    setOpen(false);
  };

  // Render each job row and handle click event to show the Dialog
  const renderRow = (summary, index) => (
    <TableRow key={index} onClick={handleClickOpen}>
      <TableCell component="th" scope="row">{index + 1}</TableCell>
      <TableCell>{summary.substring(0, 25) + "..."}</TableCell>
    </TableRow>
  );

  return (
    <Box sx={{ m: 2 }}>
      <Typography variant="h4">Likes Page</Typography>
      
      <Box sx={{ mt: 2, mb: 4 }}>
        <Typography variant="h6">Super Likes</Typography>
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>#</TableCell>
                <TableCell>Summary</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {superlikes.length > 0 ? superlikes.map(renderRow) : <TableRow><TableCell>You haven't given any super likes yet!</TableCell></TableRow>}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>

      <Box sx={{ mt: 4 }}>
        <Typography variant="h6">Likes</Typography>
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>#</TableCell>
                <TableCell>Summary</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {likes.length > 0 ? likes.map(renderRow) : <TableRow><TableCell>You haven't given any likes yet!</TableCell></TableRow>}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>

      {/* Dialog to show a message */}
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Job Notification</DialogTitle>
        <DialogContent>
          <DialogContentText>
            In production this would lead to Apply page.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Close
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

export default LikesPage;

