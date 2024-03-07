import React from 'react';
import ThreadObject from './Thread_Object';

function ThreadContainer({threads, onSave, onDelete}){

    const renderThread = threads.map((threadObj) => {
        return(
            <div key={threadObj.id}>
                <ThreadObject {...threadObj} onSave={onSave} onDelete={onDelete}/>
            </div>
        )
    })
    
    return(
        <div>
            <h1>Threads</h1>
            {renderThread}
        </div>
    )
}

export default ThreadContainer;