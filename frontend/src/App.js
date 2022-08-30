import React, { Fragment, useState , useRef, useEffect} from "react";
import axios from 'axios'
import {Form,FormGroup,Label,FormText,Input} from "reactstrap";
import './App.css'
import { FileUpload } from 'primereact/fileupload';
import { Toast } from 'primereact/toast';
import { Button } from 'primereact/button';
import { Divider } from 'primereact/divider';
async function postImage({image, description}) {
  const formData = new FormData();
  formData.append("image", image)
  formData.append("description", description)

  const result = await axios.post('/images', formData, { headers: {'Content-Type': 'multipart/form-data'}})
  return result.data
}


function Upload() {

  const [file, setFile] = useState()
  const [description, setDescription] = useState("")
  const [images, setImages] = useState([])
  const [fileName, setFileName] = useState()
  const [texto, setTexto] = useState("")

  const CargarPDF = async event => {
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
  const [totalSize, setTotalSize] = useState(0);
    const toast = useRef(null);
    const fileUploadRef = useRef(null);
    const onUpload = () => {
        toast.current.show({severity: 'info', summary: 'Success', detail: 'File Uploaded'});
    }
  
  

  return (
    <div class="md:p-6 align-items-center ">
      <Divider align="center">
        <div className="inline-flex align-items-center">
          <i className="pi pi-map-marker mr-2"></i>
          <b>Cargar Contrato</b>
          </div>
      </Divider>
      <div  class="md:p-6 align-items-center "  >
            <input onChange={fileSelected} type="file" accept="image/*"></input>
                <div className="card">
                      
                        <FileUpload mode="basic" cancelOptions="display: none"  skinSimple="true"  cancelLabel="Cancelar" chooseLabel="Seleccionar Archivo" uploadLabel="." onBeforeSelect={fileSelected}  />
                        
                </div>
              <Button  type="button" className="mr-3 p-button-raised" onClick={CargarPDF}>Cargar</Button>
            <Label>{texto}</Label>
        </div>  
       
      <Divider align="center">
                    <div className="inline-flex align-items-center">
                        <i className="pi pi-map-marker mr-2"></i>
                        <b>Lugares Declarados</b>
                    </div>
      </Divider>
      

      { images.map( image => (
        <div key={image}>
          <img src={image}></img>
        </div>
      ))}

      

    </div>
    
  );
}

export default Upload;
