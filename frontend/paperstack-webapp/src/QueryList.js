import React, {useState} from 'react';
import { Box, Stack, 
    Tabs, Tab, 
    Table, TableContainer,
    TableHead, TableBody, TableRow, TableCell,
    InputLabel, TextField, Typography} from '@mui/material';
import './QueryList.css';
import DocList from './DocList.js';

function QueryList(props) {
    const [value, setValue] = useState(1);
    const tabChanged = (event, newValue) => {
        console.log('New value: ', newValue);
        setValue(newValue);
    };

    return (<Stack>
        <Typography variant="h4">Server / Query</Typography>
        <Tabs className="ServerQueryTabs" value={value} onChange={tabChanged} lg={{ border: '1 solid grey'}}>
            <Tab label="Server" value={1}/>
            <Tab label="Query" value={2}/>
        </Tabs>
        <Box className="ServerQueryPanel" minHeight={100}>
        <Box value={value} index={1} hidden={value!==1}>
            <TextField id="server-host" label="Server host: " variant="outlined"></TextField>
            <TextField id="server-port" label="Server port" variant="filled"></TextField>
        </Box>
        <Box value={value} index={2} hidden={value!==2}>
            Query:
        </Box>
        </Box>
        <DocList />

    </Stack>);
}

export default QueryList;
