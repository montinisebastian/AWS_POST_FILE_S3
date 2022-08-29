import { useState } from 'react'
import axios from 'axios'
import {Button,Form,FormGroup,Label,FormText,Input} from "reactstrap";
import './App.css'

async function postImage({image, description}) {
  const formData = new FormData();
  formData.append("image", image)
  formData.append("description", description)

  const result = await axios.post('/images', formData, { headers: {'Content-Type': 'multipart/form-data'}})
  return result.data
}


function App() {

  const [file, setFile] = useState()
  const [description, setDescription] = useState("")
  const [images, setImages] = useState([])
  const [fileName, setFileName] = useState()
  const [texto, setTexto] = useState("")

  const submit = async event => {
    event.preventDefault()
    const result = await postImage({image: file, description})
    setImages([result.image, ...images])
    const response= await  fetch(
      'https://4mnrug2v8j.execute-api.us-east-1.amazonaws.com/Production/ocr',
      {
      method: "POST",
      headers: {
          Accept : "application/json",
          "Content-Type": "application.json"
      },
      body : JSON.stringify(fileName)
     
      }
     
    );
    const OCRBody = await response.json();
    console.log("OCRBody",OCRBody);
    setTexto(OCRBody.body[1])
  }

  const fileSelected = event => {
    const file = event.target.files[0]
		setFile(file)
    setFileName(event.target.files[0].name)
    console.log(event.target.files[0].name)
	}
  
  
  

  return (
    <div className="App">
      <form onSubmit={submit}>
        <input onChange={fileSelected} type="file" accept="image/*"></input>
        
        <button type="submit">Cargar</button>
        <Label>{texto}</Label>
      </form>

      { images.map( image => (
        <div key={image}>
          <img src={image}></img>
        </div>
      ))}

      

    </div>
  );
}

export default App;
