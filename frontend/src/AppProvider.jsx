import React, { useState } from 'react';

export const AppContext = React.createContext();

const AppProvider = ({ children }) => {
  const [jobSummaries, setJobSummaries] = useState([]);
  const [likes, setLikes] = useState([]);
  const [superlikes, setSuperlikes] = useState([]);
  const [userHasSubmitted, setUserHasSubmitted] = useState(false);

  return (
    <AppContext.Provider value={{ jobSummaries, setJobSummaries, likes, setLikes, superlikes, setSuperlikes, userHasSubmitted, setUserHasSubmitted }}>
      {children}
    </AppContext.Provider>
  );
};

export default AppProvider;
