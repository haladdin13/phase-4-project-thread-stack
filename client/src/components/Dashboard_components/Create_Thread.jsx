import React, { useState } from 'react';
import { Formik, Form, useField } from 'formik';
import * as Yup from 'yup';

function CreateThread(props){

    const [showCreateThread, setShowCreateThread] = useState(false);

    function handleClick(){
        setShowCreateThread(!showCreateThread);
    }
    
    const ThreadTextInput = ({ label, ...props }) => {
        const [field, meta] = useField(props);
        return (
            <div className="form-group">
                <label htmlFor={props.id || props.name}>{label}</label>
                <input className='text-input' {...field} {...props} />
                {meta.touched && meta.error ? (
                    <div className="error">{meta.error}</div>
                ) : null}
            </div>
        );
    }
    


        return (
        <div>
            {showCreateThread ? (
            <Formik
                initialValues={{
                    thread_title: '',
                    thread_content: '',
                    category_id: '',
                    likes: ''
                    
                }}
                validationSchema={Yup.object({
                    thread_title: Yup.string()
                    .min(3, 'Title must be at least 3 characters long')
                    .required('Title is required'),
                    thread_content: Yup.string()
                    .min(6, 'Description must be at least 6 characters long')
                    .required('Description is required'),
                })}
                onSubmit={(values, { setSubmitting, resetForm }) => {
                    fetch('http://127.0.0.1:5555/threads', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(values),
                })
                .then(res => res.json())
                .then(newThread => {
                    props.onAddThread(newThread)
                    resetForm();
                    setSubmitting(false)
                })
          }}
        
            >
            <Form className='Form'>
                <ThreadTextInput label="Title" name="thread_title" />
                <ThreadTextInput label="Description" name="thread_content" />
                <button type="submit">Submit</button>
            </Form>

            </Formik>
            ) : null}
            <button className='Create-thread-dashboard' onClick={handleClick}>{showCreateThread ? "Cancel" : "Create A Thread"}</button>
        </div>
            )
            
}

export default CreateThread;