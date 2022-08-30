import React, { Fragment, useState , useRef, useEffect} from "react";
import { Button } from 'primereact/button';
import 'primereact/resources/themes/lara-light-indigo/theme.css';
import 'primereact/resources/primereact.css';
import 'primeflex/primeflex.css'
import Sello from '../imagenes/sellos.jpg'


function Cabecera(){

    return(
        <div  className="grid grid-nogutter surface-0 text-800">
            
            <div className="col-12 md:col-6 p-6 text-center md:text-left flex align-items-center ">
                <section>
                    <span className="block text-6xl font-bold mb-1 text-orange-500">Declaración Jurada del Impuesto al Sello</span>
                    <div className="text-6xl text-primary font-bold mb-3">Impactando en BlockChain Federal Argentina</div>
                    <p className="mt-0 mb-4 text-700 line-height-3">Existen modos de certificar contenidos a través de
        Blockchain. Estos mecanismos permiten generar una
        “prueba de existencia”, algo así como un sello digital
        que demuestra que el contenido de un mensaje existía
        antes de una fecha y hora determinada y no fue
        modificado.</p>
        
                    <Button label="Comenzar" type="button" className="mr-3 p-button-raised"  />
                    
                </section>
            </div>
            <div className="col-12 md:col-6 overflow-hidden ">
                
                <img src={Sello}  className="md:ml-auto block md:h-full max-w-full" style={{ clipPath: 'polygon(8% 0, 100% 0%, 100% 100%, 0 100%)' }} />
                
            </div>
        </div>
    )
}


export default Cabecera;