import React, { Fragment, useState , useRef, useEffect} from "react";
import axios from 'axios'
import {Form,FormGroup,Label,FormText,Input} from "reactstrap";
import './App.css'
import { FileUpload } from 'primereact/fileupload';
import { Toast } from 'primereact/toast';
import { Button } from 'primereact/button';
import { Divider } from 'primereact/divider';
import { Dropdown } from 'primereact/dropdown';
import { Fieldset } from 'primereact/fieldset';
import { InputText } from 'primereact/inputtext';
import { Dialog } from 'primereact/dialog';
import CalcularHASH256_2 from "./components/CalcularHASH256_2";
import 'primeicons/primeicons.css';
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
  const [dnis, setDNIS] = useState([])
  const [denominaciones, setDenominaciones] = useState([])

  const [datos,setDatos] = useState({
    nombre : '',
    apellido : '',
    cuit      : '',
    nombre2 : '',
    apellido2 : '',
    cuit2      : '',
    domicilioReal : '',
    superficieTerrenoCatrastro : '',
    valorUnitarioTerreno: '',
    nose : '',
    tipoPersona : 'Fisica'

   
    
});
const msgs3 = useRef(null);

const [cabecera,setCabecera] = useState({
   designacionOficial : '',
   matriculaOficial : '',
   hashAnterior : ''
})
const [acto, setActo] = useState({
   acto : null,
   baseImponible : null
})
const [partesInterviniente, setpartesIntervinientes] = useState({
   tipoDni1        : '',
   numeroDni1      : '',
   sexo1           : '',
   nombreCompleto1 : '',
   rol1            : '',
   tipoDni2        : '',
   numeroDni2      : '',
   sexo2           : '',
   nombreCompleto2 : '',
   rol2            : ''

})
const [fechas, setFechas] = useState({
   fechaDeActo : null,
   fechaActualizacionDeuda : null,
   fechaVencimiento : null
})
const [actividadComercial, setActividadComercial] = useState({
   actividad : ''
})


const [fechaDeActo, setfechaDeActo] = useState(null)

const [nuevoTitular, setNuevoTitular] = useState({
    tipoPersona2 : 'Juridica'    
})

const [inmueble, setInmueble] = useState({
    numeroInmueble : ''   
})
const [hashes,setHash]=useState({
    hash :          '',
    hashRespaldo :  ''
})

const [lugares, setLugares] = useState({
    provinciaOtorgamiento : 'Seleccione Provincia',
    provinciaCumplimiento : 'Seleccione Provincia'
})
const [provinciaSeleccionada, setprovinciaSeleccionada] = useState(null);
const [provinciaFiltrada, setprovinciaFiltrada] = useState(null);
const [verificacion,setVerificado] = useState({
    stamps : []
});

const [tiempoLenguajeNatural,setTiempoLenguajeNatural] = useState({
    tiempo : 'sinTiempo'
});

  const arrayDnis = [];
  const tipoDNIs = ['DNI', 'CUIT', 'CUIL', 'CDI'];
  const roles = ['Acreedor', 'Deudor'];
  const sexo  = ['Masculino', 'Femenino'];
  const handleInputChange = (event) => {
        
    event.preventDefault()
    setActo({
        ...acto,
        [event.target.name] : event.target.value
    })
    setLugares({
        ...lugares,
        [event.target.name] : event.target.value
    })

    setpartesIntervinientes({
        ...partesInterviniente,
        [event.target.name] : event.target.value
    })
    //console.log(event.target.value)
    setDatos({
        ...datos,
        [event.target.name] : event.target.value
    })
    /*setNuevoTitular({
        tipoPersona2 : event.target.value
    })*/
    setCabecera({
        ...cabecera,
        [event.target.name] : event.target.value
    })
    setInmueble({
        ...inmueble,
        [event.target.name] : event.target.value    
    })
    setFechas({
        ...fechas,
        [event.target.name] : event.target.value
    })
    setActividadComercial({
        ...actividadComercial,
        [event.target.name] : event.target.value
    })
    setHash({
        hashRespaldo : (cabecera.designacionOficial+cabecera.matriculaOficial+cabecera.hashAnterior+
        datos.nombre+datos.cuit+datos.tipoPersona+
        datos.nombre2+datos.cuit2+datos.tipoPersona2+
        datos.domicilioReal+datos.superficieTerrenoCatrastro+datos.valorUnitarioTerreno+inmueble.tipoInmueble
        +lugares.provinciaOtorgamiento+lugares.provinciaCumplimiento+
        partesInterviniente.tipoDni1+partesInterviniente.numeroDni1+partesInterviniente.sexo1+partesInterviniente.nombreCompleto1+partesInterviniente.rol1+
        partesInterviniente.tipoDni2+partesInterviniente.numeroDni2+partesInterviniente.sexo2+partesInterviniente.nombreCompleto2+partesInterviniente.rol2+
        fechas.fechaDeActo+fechas.fechaActualizacionDeuda+fechas.fechaVencimiento+acto.acto+acto.baseImponible+
        actividadComercial.actividad+
        inmueble.numeroInmueble),
        
        hash : CalcularHASH256_2(hashes.hashRespaldo)
})
    
    
    
    
    
  }
  const renderFooter = (name) => {
    return (
        <div>
            
            <Button label="Continuar" icon="pi pi-check" onClick={() => onHide(name)} autoFocus />
        </div>
    );
   }






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
    setTexto(OCRBody.body[1]);
    setDNIS(OCRBody.body[2].split(','));
    setDenominaciones(OCRBody.body[3].split(','));
    
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
    const [displayResponsive, setDisplayResponsive] = useState(false);
    const [displayDialogoResultadosIntervinientes, setDisplayDialogoResultadosIntervinientes] = useState(false);
    const [displayDialogoResultadosLugaresDestacados, setDisplayDialogoResultadosLugaresDestacados] = useState(false);
    const [displayDialogoResultadosImpuesto, setDisplayDialogoResultadosImpuesto] = useState(false);
    const dialogFuncMap = {
   
      'displayResponsive': setDisplayResponsive,
      'displayDialogoResultadosIntervinientes' : setDisplayDialogoResultadosIntervinientes,
      'displayDialogoResultadosLugaresDestacados' : setDisplayDialogoResultadosLugaresDestacados,
      'displayDialogoResultadosImpuesto' : setDisplayDialogoResultadosImpuesto
    }
  
  const onClick = (name, position) => {
      dialogFuncMap[`${name}`](true);

      if (position) {
          setPosition(position);
      }
  }  
  function mostrarDialogoResultadosIntervinientes() {
      onClick('displayDialogoResultadosIntervinientes');
  }
  function mostrarDialogoResultadosLugaresDestacados() {
      onClick('displayDialogoResultadosLugaresDestacados');
  }
  function mostrarDialogoResultadosImpuesto(){
      onClick('displayDialogoResultadosImpuesto')
  }
  const [position, setPosition] = useState('center');
  const onHide = (name) => {
    dialogFuncMap[`${name}`](false);
  }
  
  
  
  return (
    <div class="md:p-6 align-items-center ">
      <Divider align="center">
        <div className="inline-flex align-items-center">
          <i className="pi pi-map-marker mr-2"></i>
          <b>Cargar Contrato</b>
          </div>
      </Divider>
      <Divider align="center">
      <div  class="md:p-6 align-items-center "  >
            <input onChange={fileSelected} type="file" accept="image/*"></input>
                <div className="card">
                      
                        <FileUpload mode="basic" cancelOptions="display: none"  skinSimple="true"  cancelLabel="Cancelar" chooseLabel="Seleccionar Archivo" uploadLabel="." onBeforeSelect={fileSelected}  />
                        
                </div>
              <Button  type="button" className="mr-3 p-button-raised" onClick={CargarPDF}>Cargar</Button>
            <Label>Listado de DNIS:{dnis}</Label>
            <Label>Listado de denominaciones:{denominaciones}</Label>
        </div>  
        </Divider>
      


      <div  class="md:p-6 align-items-center "  >

            <Divider align="center">
                    <div className="inline-flex align-items-center">
                        <i className="pi pi-home mr-2"></i>
                        <b>Partes Intervinientes</b>
                    </div>
            </Divider>

      </div>

      

      <div  class="md:p-6 align-items-center "  >
            <Fieldset legend="Primer Interviniente">
      <div class="p-fluid grid">
      <div class="field col-12 md:col-4">
            <label htmlFor="TipoDocumento" className="block">Tipo de Documento</label> 
            
                <Dropdown tooltip={hashes.hash} name="tipoDni1" value={partesInterviniente.tipoDni1} options={tipoDNIs} onChange={handleInputChange}  placeholder="Seleccione Tipo Documento" />

            </div>

            <div class="field col-12 md:col-4">   
            
                    <label htmlFor="SuperficieTerrenoCatrastro" className="block">Numero de Documento</label>
                    <Dropdown tooltip={hashes.hash} id="NumeroDocumento1" value={partesInterviniente.numeroDni1} name="numeroDni1" options={dnis}  onChange={handleInputChange} placeholder="Ingrese Numero de Documento" editable/>
                   
                
            </div>
            <div class="field col-12 md:col-4">
            <label htmlFor="DomicilioReal" className="block">Sexo</label> 
            
                <Dropdown tooltip={hashes.hash} name="sexo1" value={partesInterviniente.sexo1} options={sexo} onChange={handleInputChange} placeholder="Seleccione Sexo" />

            </div>
            <div class="field col-12 md:col-4">   
            
                    <label htmlFor="SuperficieTerrenoCatrastro" className="block">Nombre Completo</label>
                    <InputText tooltip={hashes.hash} id="NombreCompleto1" name="nombreCompleto1"  onChange={handleInputChange} placeholder="Ingrese Nombre Completo"/>
                   
                
            </div>
            <div class="field col-12 md:col-4">
            <label htmlFor="Roles" className="block">Rol</label> 
            
                <Dropdown tooltip={hashes.hash} name="rol1" value={partesInterviniente.rol1} options={roles} onChange={handleInputChange}   placeholder="Seleccione Rol"/>

            </div>
            
            </div>
            
            </Fieldset>
        </div>


        <div  class="md:p-6 align-items-center "  >
            <Fieldset legend="Segundo Interviniente">
            <div class="p-fluid grid">   
            
            <div class="field col-12 md:col-4">
            <label htmlFor="TipoDocumento" className="block">Tipo de Documento</label> 
            
                <Dropdown tooltip={hashes.hash} name="tipoDni2" value={partesInterviniente.tipoDni2} options={tipoDNIs} onChange={handleInputChange}  placeholder="Seleccione Tipo Documento" />

            </div>

            <div class="field col-12 md:col-4">   
            
                    <label htmlFor="SuperficieTerrenoCatrastro" className="block">Numero de Documento</label>
                    <Dropdown tooltip={hashes.hash} id="NumeroDocumento2" name="numeroDni2" value={partesInterviniente.numeroDni2}   options={dnis} onChange={handleInputChange} placeholder="Ingrese Numero de Documento"/>
                   
                
            </div>
            <div class="field col-12 md:col-4">
            <label htmlFor="DomicilioReal" className="block">Sexo</label> 
            
                <Dropdown tooltip={hashes.hash} name="sexo2" value={partesInterviniente.sexo2} options={sexo} onChange={handleInputChange} placeholder="Seleccione Sexo" />

            </div>
            <div class="field col-12 md:col-4">   
            
                    <label htmlFor="SuperficieTerrenoCatrastro" className="block">Nombre Completo</label>
                    <InputText tooltip={hashes.hash} id="NombreCompleto2" name="nombreCompleto2"  onChange={handleInputChange} placeholder="Ingrese Nombre Completo"/>
                   
                
            </div>
            <div class="field col-12 md:col-4">
            <label htmlFor="Roles" className="block">Rol</label> 
            
                <Dropdown tooltip={hashes.hash} name="rol2" value={partesInterviniente.rol2} options={roles} onChange={handleInputChange}   placeholder="Seleccione Rol"/>

            </div>
            <div class="field col-12 md:col-4 pt-5" >
                
                <Button icon="pi pi-plus" label="Cargar Datos" type="button" className="tipoPersona" onClick={() => mostrarDialogoResultadosIntervinientes()} />
                
                <Dialog header="Carga de Partes Intervinientes con Exito" visible={displayDialogoResultadosIntervinientes} onHide={() => onHide('displayDialogoResultadosIntervinientes')} breakpoints={{'960px': '75vw'}} style={{width: '50vw'}} footer={renderFooter('displayDialogoResultadosIntervinientes')}>
                        <h3>Primer Interviniente</h3>
                        <p><b>Tipo Documento: </b>  {partesInterviniente.tipoDni1}</p>
                        <p><b>Número: </b>          {partesInterviniente.numeroDni1}</p>
                        <p><b>Nombre Completo: </b> {partesInterviniente.nombreCompleto1}</p>
                        <p><b>Sexo:             </b>{partesInterviniente.sexo1}</p>
                        <p><b>Rol: </b>             {partesInterviniente.rol1}</p>
                        <p>------------------------------------------------------------------------------</p>
                        <h3>Segundo Interviniente</h3>
                        <p><b>Tipo Documento: </b>  {partesInterviniente.tipoDni2}</p>
                        <p><b>Número: </b>          {partesInterviniente.numeroDni2}</p>
                        <p><b>Nombre Completo: </b> {partesInterviniente.nombreCompleto2}</p>
                        <p><b>Sexo: </b>            {partesInterviniente.sexo2}</p>
                        <p><b>Rol: </b>             {partesInterviniente.rol2}</p>
                </Dialog>
            </div>
            
            </div>
            
            </Fieldset>
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
