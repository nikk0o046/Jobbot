import React, { createContext, useState } from 'react';

export const AppContext = createContext();

const AppProvider = ({ children }) => {
  const [likes, setLikes] = useState([]);
  const [superlikes, setSuperlikes] = useState([]);
  const [jobSummaries, setJobSummaries] = useState([]);

  return (
    <AppContext.Provider 
      value={{ 
        likes, 
        setLikes, 
        superlikes, 
        setSuperlikes, 
        jobSummaries, 
        setJobSummaries 
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export default AppProvider;
