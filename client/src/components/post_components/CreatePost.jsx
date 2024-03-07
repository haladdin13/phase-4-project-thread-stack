import React, { useState } from 'react';
import { Formik, Form, useField } from 'formik';
import * as Yup from 'yup';

function CreatePost(props){

    const [showCreatePost, setShowCreatePost] = useState(false);

    function handleClick(){
        setShowCreatePost(!showCreatePost);
    }
    
    const PostTextInput = ({ label, ...props }) => {
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
            {showCreatePost ? (
            <Formik
                initialValues={{
                    content: ''
                }}
                validationSchema={Yup.object({
                    content: Yup.string()
                    .min(1, 'Name must be at least 1 characters long')
                    .required('Name is required'),
                })}
                onSubmit={(values, { setSubmitting, resetForm }) => {
                    fetch('http://localhost:5555/posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(values),
                })
                .then(res => res.json())
                .then(newPost => {
                    props.onAddPost(newPost)
                    resetForm();
                    setSubmitting(false)
                })
          }}
        
            >
            <Form>
                <PostTextInput label="Name" name="content" />
                <button type="submit">Submit</button>
            </Form>

            </Formik>
            ) : null}
            <button onClick={handleClick}>{showCreatePost ? "Cancel" : "Create A Post"}</button>
        </div>
            )
            
}

export default CreatePost;