import React, { useContext } from 'react';
import { AppContext } from '../AppProvider'; // Import the AppContext
import { Box, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

function LikesPage() {
  const { superlikes, likes } = useContext(AppContext); // Use the context

  const renderRow = (summary, index) => (
    <TableRow key={index}>
      <TableCell component="th" scope="row">{index + 1}</TableCell>
      <TableCell>{summary.substring(0, 25) + "..."}</TableCell>
    </TableRow>
  );

  return (
    <Box sx={{ m: 2 }}> {/* Add margin */}
      <Typography variant="h4">Likes Page</Typography>
      <Box sx={{ mt: 2, mb: 4 }}> {/* Add margin to Box */}
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
      <Box sx={{ mt: 4 }}> {/* Add margin to Box */}
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
    </Box>
  );
}

export default LikesPage;
