import re
import io
documento2 = """CONTRATO DE LOCACION
ENTRE el Sr. OSCAR FRANCISCO IGLESIAS CUIL N° 20-10376645-2 de nacionalidad argentina,
mayor de edad, por una parte y en adelante denominado la LOCADORA, y por la otra la Sra.
CANDELA MARIA MUIÑO CUIL N° 27-41846026-7 de nacionalidad argentina, mayor de edad, en
adelante denominado la LOCATARIA, se ha convenido en celebrar el presente contrato de locación
que se regirá por las disposiciones del Código Civil y Comercial de la Nación, sus modificaciones y por
las siguientes cláusulas:
PRIMERA - OBJETO: La LOCADORA cede en locación a la LOCATARIA quien acepta de conformidad en
tal carácter el inmueble sito en calle MARCELO T. DE ALVEAR N° 267 - 11° PISO DPTO. "A" -
CORDOBA, compuesto de un dormitorio: con placar; baño: completo totalmente instalado con
bañera; hall: con placar; living comedor; cocina: con mesada de granito natural, bacha de acero
inoxidable, bajo mesada con puertas de madera, una cocina marca VOLCAN y un calefón marca ORBIS
12 Its. a corredera. Los artefactos se encuentran en buen estado y funcionando.
SEGUNDA - DESTINO: El destino del uso se conviene exclusivamente para vivienda familiar de la
LOCATARIA.
TERCERA - PLAZO CONTRACTUAL: El término de la locación se conviene en TREINTA Y SEIS (36)
MESES contados a partir del día PRIMERO DE JULIO DE DOS MIL VEINTIDOS (01-07-2022)
venciendo en consecuencia el día TREINTA DE JUNIO DE DOS MIL VEINTICINCO (30-06-2025)
fecha en que la LOCATARIA deberá restituir a la LOCADORA y/o quien la represente el inmueble locado
en las condiciones pactadas en el presente. La recepción del mismo por parte de la LOCADORA aún sin
reserva alguna de su parte, no implicará conformidad con el estado del inmueble por lo que la
LOCATARIA deberá requerir un comprobante de recepción en el que conste expresamente
la
conformidad de la LOCADORA.
CUARTA - PRECIO: El precio del Alquiler será abonado por la LOCATARIA en moneda nacional corriente
de curso legal, conviniendo los contratantes que el precio inicial y provisorio por el mínimo legal de
tres (3) años totaliza la suma de pesos UN MILLON DOSCIENTOS SESENTA MIL ($ 1.260.000.-) que la
LOCATARIA abonará de la siguiente manera: a) durante los primeros doce (12) meses, es decir el
primer año locativo abonará de manera mensual y consecutiva la suma de pesos TREINTA Y CINCO
MIL ($ 35.000.-). b) Para los segundos doce (12) meses, es decir el segundo año locativo
abonará de manera mensual y consecutiva el alquiler pactado para el primer año actualizado
anualmente de forma acumulativa y progresiva por el índice conformado por partes iguales entre las
variaciones mensuales del Índice de Precios del Consumidor (IPC) y la Remuneración Imponible
Promedio de los Trabajadores Estables (RIPTE), ambos valores establecidos y publicados
mensualmente por el Banco Central de la República Argentina (BCRA) y c) Para los terceros doce
(12) meses, es decir el tercer año locativo abonará de manera mensual y consecutiva el monto del
alquiler obtenido para el segundo año actualizado anualmente de forma acumulativa y progresiva por
el índice conformado por partes iguales entre las variaciones mensuales del Índice de Precios del
Consumidor (IPC) y la Remuneración Imponible Promedio de los Trabajadores Estables (RIPTE), ambos
valores establecidos y publicados mensualmente por el Banco Central de la República Argentina
(BCRA). Si a la fecha de vencimiento del pago del primer mes del segundo y el tercer año, no se
hubiese efectuado aún la publicación respectiva, el LOCATARIO abonara el monto que venía abonando
durante el último mes del año anterior con carácter provisorio; debiendo integrar la diferencia que
surja de la aplicación de dicho índice dentro de las cuarenta y ocho (48) horas hábiles posteriores
contadas desde la fecha que resulte publicado el mismo. Además del monto pactado, quedan a cargo
exclusivo de la LOCATARIA y deberán considerarse formando parte del precio de la locación los
servicios de agua corriente, de energía eléctrica y gas natural; gastos comunes (expensas ordinarias:
administración, portero, services varios, luz, pintura, vigilancia, seguro, desagotes, etc.)
QUINTA - MODALIDAD, FECHA Y LUGAR DE PAGO: El alquiler mensual será abonado por
mes
adelantado el día primero de cada mes quedando establecido que el mero vencimiento del plazo, hará
incurrir en mora de pleno derecho. La LOCADORA otorga plazo de gracia hasta el día diez de cada mes,
período en el cual la LOCATARIA podrá abonar sin ningún tipo de recargo, vencido dicho plazo de
gracia, los intereses punitorios se percibirán desde la fecha de vencimiento en el domicilio de
la LOCADORA Arturo M. Bas 43 PB 1, lunes a viernes de 10 a 13 o bien donde posteriormente ésta lo
indique, debiendo abonarse por períodos de meses enteros. Así mismo deberá abonar en término
todos los impuestos y tasas que no graven el inmueble, servicios y gastos comunes, ya que además
del precio pactado en pesos se incluye como parte integrante de la locación el pago de los mismos,
como condición previa al pago del alquiler, debiendo entregar los comprobantes originales de pago y/o
reintegrar los importes que hubiere abonado por tales conceptos la LOCADORA, con más intereses,
multas y actualizaciones si correspondieran. El incumplimiento de la LOCATARIA faculta a
la
LOCADORA a no admitir el pago del alquiler y/o a dar por rescindido el presente contrato y a exigir su
cobro por la vía ejecutiva.
1
SEXTA - PUNITORIOS: El mero vencimiento del plazo hará incurrir en mora a la LOCATARIA en forma
automática, sin necesidad de interpelación previa judicial o extrajudicial alguna, haciéndola pasible
de
un interés punitorio, al momento equivalente a la tasa de interés de Plazo Fijo establecida por el Banco
de la Nación Argentina sobre el monto adeudado de alquiler mensual y/o cualquier otra suma de dinero
a que se obliga la LOCATARIA, sin perjuicio de las acciones judiciales que correspondieran además de
la acción de desalojo.
SEPTIMA - ESTADO DEL INMUEBLE: La LOCATARIA que no ocupó antes la unidad locada y que no fue
inquilina de fecha anterior a la celebración de este contrato, recibe el inmueble en buen estado
de
conservación e higiene, recién reparado, declarando formalmente su conformidad con el mismo en
virtud de haberlo revisado e inspeccionado con antelación, siendo su obligación mientras dure en la
ocupación de la unidad locada y hasta que la misma sea restituida a la LOCADORA libre de ocupantes
y
de cosas, el mantenimiento y conservación de la misma; todas las refacciones, reparaciones
y
reposiciones menores, que fueran necesarias, tanto en sus instalaciones de agua, de electricidad y de
gas; instalaciones sanitarias, cloacales, pluviales; de sus herrajes, vidrios, cerraduras, llaves,
revoques, pisos, revestimientos y aberturas; de todos los artefactos e instalaciones que se mencionan
en la CLAUSULA PRIMERA de este contrato, etc. No pudiendo por ninguna causa o motivo exigir la
realización a la LOCADORA. Si se requieren reparaciones del inmueble la LOCATARIA deberá
comunicarlas en forma fehaciente a la LOCADORA, tomando como notificación válida el primer día hábil
posterior de emitida la notificación. Si se trata de causas urgentes la LOCADORA tendrá 24 horas para
comenzar los trabajos de reparación; si fueren no urgentes la LOCADORA dispondrá de 10 días para
iniciar la reparación. En caso de negativa o silencio de la LOCADORA, la LOCATARIA podrá realizar las
mismas a cargo de la LOCADORA, presentando presupuestos con plazos y precios acordes a los de
mercado, realizado por personal matriculado y con facturas oficiales, notificados previamente a la
LOCADORA. Es condición especial de esta locación que la LOCATARIA restituya el inmueble RECIEN
PINTADO, ya que así lo recibe, El inmueble se entrega con la pintura en el siguiente estado:
INTERIORES: paredes, interiores de los placares y cielorrasos, con pintura marca FADEPA para
interiores, color blanco recién pintados; los MARCOS de las aberturas recién pintadas con sintético
color marrón; PUERTAS placas todas recién lustradas inclusive las de PLACARES DE DORMITORIOS,
azulejos del baño y cocina recién pintados; EL LOCATARIO se compromete a entregar al LOCADOR al
momento de desocupar el inmueble los litros de pintura látex blanco para interior marca FADEPA, así
como los demás materiales necesarios y la cantidad de pesos necesarios para contratar la mano de
obra para realizar la pintura completa de la unidad. Para ello se solicitarán 3 presupuestos a
profesionales en la materia, para establecer el exacto monto del trabajo a realizar. El LOCATARIO
deberá entregar la vivienda desocupada, cinco (5) días hábiles antes de finalizar el contrato, para
realizar las tareas de pintura. Estos trabajos deberán ser realizados por personal idóneo a plena
conformidad de la LOCADORA. Convienen las partes que no se considerará terminada la locación por
parte de la LOCATARIA mientras no haya cumplido con todos estos requisitos, quedando obligada
a
satisfacer el alquiler mensual por el tiempo que transcurra hasta que los desperfectos o deterioros
sean reparados y el inmueble sea entregado en el mismo estado en que lo recibió.
OCTAVA - OBLIGACIONES DE LA LOCATARIA: Son obligaciones de la LOCATARIA: 1°) Cumplimentar
todas la estipulaciones expresadas en las cláusulas de este contrato; 2°) Solicitar el servicio de energía
eléctrica y gas natural a su nombre en un término de diez días de la fecha de iniciación del presente,
siendo a su cargo todo gasto que ello origine debiendo presentar a la LOCADORA y/o quien
la
represente el alta de dicho servicio dentro de los primeros treinta (30) días del presente; solicitar la
baja de estos servicios dentro de los treinta (30) días anteriores a la fecha de entrega de las llaves de
la propiedad y hacer entrega a la LOCADORA y/o quien la represente de la constancia de las mismas al
momento de hacer entrega del bien en las condiciones pactadas. Si la LOCATARIA no cumplimentare
con lo anteriormente pactado será responsable por los daños y perjuicios que le ocasionare a la
LOCADORA esta omisión, siendo de su exclusivo cargo el pago de facturas, recargos, multas, ilícitos,
honorarios, cargo por mano de obra y materiales e inspecciones si diera lugar al corte del suministro,
etc.; 3°) Abonar con puntualidad los servicios de agua, energía eléctrica y gas natural a las empresas
que los suministren; 4°) Abonar con puntualidad las expensas ordinarias a la administración del
consorcio presentar a la LOCADORA y/o quien la represente los comprobantes abonados de las
mismas, al momento de hacer entrega del inmueble la LOCATARIA deberá presentar libre de deuda de
las mismas otorgado por la administración del consorcio; 5°) Abonar los impuestos nacionales,
provinciales, municipales, tasas o sobretasas, creados o que pudieran crearse que no graven el
inmueble; 6°) Abonar las costas, gastos y honorarios judiciales o extrajudiciales de todo procedimiento
a que dé lugar el incumplimiento del presente contrato; 7°) Respetar todas la disposiciones,
reglamentaciones u ordenanzas de cualquier orden, vigentes o futuras, relativas a la normal
convivencia, de policía edilicia y demás, haciéndose responsable de cualquier violación a las mismas;
8°) Permitir a la LOCADORA y/o quien la represente a visitar el inmueble cuantas veces lo estime
necesario a los fines de inspeccionar, verificar el estado de conservación, efectuar algún trabajo en el
mismo, como así también con terceros interesados en la locación durante los últimos quince días
previos a la finalización o resolución anticipada del presente; 9°) Poner en comunicación de la
LOCADORA en un plazo no mayor de 24 horas de producido cualquier daño, perjuicio o deterioro en la
propiedad ya sea urgente, no urgente, o por culpa de terceros, sin perjuicio de la obligación de la
LOCATARIA de repararlos si así le corresponde conforme lo establece la CLAUSULA SEPTIMA del
presente; 10°) Cargar con los gastos de reparación del inmueble, sus colindantes o personas en
el
2
caso de incendio, explosiones, filtraciones, humedades y desmoronamientos o cualquier otro daño que
se produjeran por culpa, imprudencia o negligencia de la LOCATARIA o de las personas que
ocupen o concurran al inmueble, siendo por cuenta de la LOCATARIA el asegurar la propiedad contra
todos estos riesgos, como así también todas las reparaciones que fueran necesarias en caso de robos y
hurtos; 11°) Abonar todos los gastos que demanden el desagote de la cámara séptica;
12°)
Presentarse a solicitud de la LOCADORA ante las empresas prestatarias de servicios en caso de que
fuera menester, como así mismo a homologar el vencimiento de este contrato; 13°) Cumplimentar
legal y patrimonialmente toda disposición de cualquier orden que exija o exigiere el acondicionamiento
de la unidad locada al destino de afectación que la LOCATARIA dé a la misma, no pudiendo por
ninguna causa exigir su realización o erogación a la LOCADORA, quedando todo en beneficio de la
propiedad, sin derecho a indemnización o retribución alguna; 14°) Abonar todos los impuestos, tasas,
sobretasas y contribución por mejoras, sean éstas de cualquier orden, que graven el inmueble como
consecuencia de la actividad que en el mismo desarrolla la LOCATARIA; 15°) Respetar estrictamente
las normas de fondo respecto de la propiedad horizontal, todas las disposiciones del Reglamento de
Copropiedad como así también del Reglamento Interno del lugar, cuyos contenidos declara conocer y
aceptar; 16°) En el supuesto que depositare judicialmente las llaves del inmueble, estarán a su cargo
todas las diligencias conducentes a otorgarle a la LOCADORA la tenencia, previa constatación del
estado del bien, subsistiendo las obligaciones de pago conforme las cláusulas suscritas y hasta que el
mismo se encuentre en las condiciones establecidas en el contrato; 17°) Si por una disposición legal
y
futura los arriendos se vieren gravados con el pago del impuesto al valor agregado (IVA), la
LOCATARIA deberá adicionar al monto mensual a ingresar en concepto de canon locativo, el porcentual
correspondiente al IVA; 17°) La LOCATARIA deberá presentar y/o abonar en el domicilio de pago, a la
finalización del contrato de locación, un informe realizado por un gasista MATRICULADO, el cual deberá
dejar expresa constancia del correcto funcionamiento de todos los artefactos que operen con gas como
así también de sus respectivas conexiones. Esta cláusula se aplicara siempre y cuando el propietario
realice por su cuenta y cargo la primera inspección.
NOVENA - PROHIBICIONES DE LA LOCATARIA: Le queda absolutamente prohibido a la LOCATARIA: a)
Destinar la unidad locada a otra afectación que la pactada en la CLAUSULA SEGUNDA del presente; b)
No podrá por ninguna causa ejercer el derecho de retención de la unidad ni de los alquileres, haciendo
expresa renuncia al mismo; c) Toda forma de transferencia o cesión, sea de manera parcial o total;
sublocar, prestar, permutar, hacerse reemplazar por terceros cualquiera sea el grado de relación
o
consanguinidad; constituirse o fusionarse con terceros, personalmente o formando sociedades; d)
Efectuar modificaciones o mejoras de ninguna naturaleza que alteren la estructura actual del inmueble
sin consentimiento previo fehaciente de la LOCADORA. Si así lo hiciere, las mejoras realizadas
quedaran en beneficio de la propiedad sin derecho a indemnización o compensación alguna, o deberá
reconstruir al estado anterior, a conformidad de la LOCADORA. Para el caso que la LOCADORA las
autorice por escrito, la LOCATARIA deberá presentar presupuestos a consideración de la LOCADORA,
debiendo esta ultima reembolsar a la LOCATARIA lo invertido. e) Exigir a la LOCADORA la realización
de mejoras que se carecieran al día de la fecha, por ej.: redes internas o externas de gas, cloacas
o
cualesquier otro servicio; f) La LOCATARIA no podrá informar por su cuenta la existencia del contrato
a
la AFIP sin antes requerir en modo fehaciente al LOCADOR el cumplimiento de esta obligación,
otorgándole al efecto un plazo no inferior a veinte (20) días, quedando relevado el administrador de
tal
obligación.
DECIMA - OBLIGACIONES DEL LOCADOR: 1°) Respetar las obligaciones contractuales y legales
asumidas por el presente contrato, 2°) Abonar el Impuesto Inmobiliario Municipal, Impuesto
Inmobiliario Provincial y/o cualquier otro que grave la cosa. 3°) Declarar la celebración del presente
contrato de locación a la Administración Federal de Ingresos Públicos (AFIP), relevando al
Administrador de tal obligación.
DECIMO PRIMERA - FRUSTRACION DEL USO O GOCE DE LA COSA: La LOCADORA no se responsabiliza
por los daños, deterioros y demás que pudiera sufrir dentro de la propiedad las personas o cosas
puestas por la LOCATARIA o que de ella dependan. Si por alguna causa no imputable a la LOCATARIA y
solo en relación al estado del inmueble, esta se ve imposibilitada de usar o gozar del mismo, ante
la
previa notificación, silencio o negativa de la LOCADORA para efectuar alguna reparación urgente,
la
LOCATARIA podrá pedir la cesación de pago o rescisión del contrato según Art. 1203 del CCCN.
DECIMO SEGUNDA - MULTA INDEMNIZATORIA: Si al término de este contrato la LOCATARIA no hiciere
entrega de la propiedad locada libre de ocupantes o de cosas, sin deudas y en las condiciones
pactadas, o efectuara consignación de llaves o diera lugar a una acción legal, continuará abonando el
alquiler con el mecanismo y pautas establecidas en la CLAUSULA CUARTA con más una multa mensual
indemnizatoria equivalente a tres (3) veces el importe del último alquiler que le hubiera correspondido
abonar según este contrato, suma ésta independiente de las acciones de desalojo y por daños y
perjuicios que correspondan. La multa regirá hasta el día en que la LOCADORA tome posesión real
y
efectiva del inmueble a su entera satisfacción y sin que ello signifique o pueda interpretarse como
novación, prórroga automática o indefinida, pacto de opción ni tácita reconducción, ni locación de plazo
indeterminado.
3
DECIMO TERCERA - ABANDONO MANIFIESTO: Las partes acuerdan para el caso de abandono
manifiesto del inmueble que la LOCADORA podrá retomar la tenencia del mismo previo inventario y/o
constatación por ante Escribano Público. Subsistiendo las obligaciones de pago conforme las cláusulas
suscritas y hasta que el mismo se encuentre en las condiciones establecidas en el contrato.
DECIMO CUARTA - GARANTIA: Los esposos: la Sra. EMMA ELENA DE MARIA MINI DNI N°
17.045.152.- y el Sr. ORLANDO MANUEL MUIÑO DNI N° 12.810.012.- aceptados ambos en
su
calidad de empleados y propietarios del inmueble inscripto bajo la Matrícula N° 157.959/20.-, fijando
ambos domicilio especial a todos los efectos legales en calle Duarte Quiros N° 433 C 2 2 - B°
Centro (CP. 5000), Córdoba; y en segunda instancia fijando domicilio electrónico
emma.mini@hotmail.es y orlamui@hotmail.com; suscribe/n este contrato constituyéndose en fiador/es
y
principal/es pagador/es de todas y cada una de las obligaciones emergentes de este contrato en una
misma e idéntica situación legal que la LOCATARIA, con renuncia expresa a los beneficios de excusión,
división, interpelación o aviso previo, cualesquiera fueran la cantidad y monto de la mensualidades
adeudadas y demás cargas y obligaciones pecuniarias, compensatorias o resarcitorias; gastos por
trámites, honorarios y costas judiciales o extrajudiciales que pudieran originarse por acciones de cobro
de alquileres, desalojo, daños y perjuicios, posesión judicial, cobro de impuestos, tasas, servicios,
expensas comunes, contribuciones especiales, deterioros, daños y perjuicios del inmueble. En
garantía de las obligaciones precedentemente asumidas, la fiadora: la Sra. EMMA ELENA DE
MARIA MINI DNI N° 17.045.152.- y el Sr. ORLANDO MANUEL MUIÑO DNI N° 12.810.012.-
afectan el inmueble de su propiedad inscripto en el Registro Gral. De La Provincia bajo la
Matrícula N° 157.959/20.-, renunciando expresamente por el presente a los derechos de
inembargabilidad e inejecutabilidad que establecen el art. 58 de la Constitución Provincial y
la Ley Provincial 8067, concordantes y modificatorias. La garantía se extiende vigente aún luego
de expirado el plazo contractual, mientras la LOCATARIA continúe ocupando la unidad y/o adeudando
suma alguna y hasta el día de la fehaciente, real y efectiva entrega del inmueble a la LOCADORA, a su
satisfacción y de acuerdo a las condiciones pactadas y sin deudas por ningún concepto y hasta la
cancelación de los juicios que hubieren. La entrega del inmueble deberá constar por escrito emanado
de la LOCADORA y/o quien la represente, no admitiéndose otro medio de prueba. Perdura la garantía
aún cuando se modifique el precio del alquiler por acuerdo de las partes, legal o judicialmente,
respondiendo así mismo por los aumentos de alquiler que la LOCATARIA conviniera al vencimiento del
plazo contractual; perdura también por permanencia de la LOCATARIA por voluntad propia o por
disposiciones estatales o por quedar comprendida en una ley de prórroga. La/s garantía/s queda/n
obligada/s a informar cualquier modificación en las condiciones patrimoniales ofrecidas, caso contrario
incurrirá/n en defraudación de garantía. La LOCADORA tendrá derecho a exigir el reemplazo de la/s
garantía/s en caso de insolvencia, fallecimiento, desaparición, incapacidad o cualquier situación que
disminuya o anule su solvencia patrimonial o laboral, o sin necesidad de expresar causa alguna. Así
mismo la LOCATARIA deberá notificar fehacientemente y de forma inmediata a la LOCADORA cualquier
modificación que vaya en detrimento de las condiciones por las cuales fueron aceptadas las garantías,
precediendo al reemplazo por otra/s de igual o mayor solvencia dentro de un término de diez días;
como así también cualquier cambio en los domicilios consignados en el presente. El incumplimiento de
notificar estas novedades y/o del reemplazo de la/s garantía/s a satisfacción de la LOCADORA dará
derecho a ésta a dar por rescindido el presente contrato.
DECIMO QUINTA - SELLADO: El sellado del presente contrato será abonado exclusivamente por la
LOCATARIA.
DECIMO SEXTA - RESOLUCION ANTICIPADA: La LOCATARIA podrá resolver el presente contrato en
tiempo y forma según lo establece art. 1221 del Código Civil y Comercial de la Nación, una vez
transcurridos los (6) seis primeros meses de vigencia del mismo, debiendo en tal caso: 1) notificar en
forma fehaciente a la LOCADORA con al menos treinta días de anticipación, su voluntad en este
sentido y 2) no adeudar suma alguna en concepto de alquileres y/o de cualesquier otro ítems a su
cargo. Si la LOCATARIA hace uso de la opción resolutoria en el primer año de vigencia de la relación
locativa, deberá abonar a la LOCADORA, en concepto de indemnización la suma equivalente a un mes
y medio del alquiler vigente al momento de hacer entrega del inmueble, y la de un solo mes si la
opción se ejercita transcurrido dicho plazo. Cuando la notificación a la LOCADORA se realiza con una
anticipación de tres meses o más, transcurridos al menos seis meses de contrato, no corresponde el
pago de indemnización alguna por dicho concepto. En este caso la LOCATARIA deberá permitir, por así
haberlo convenido con la LOCADORA, el ingreso de ésta y/o quien la represente durante los últimos
treinta (30) días del aviso fehaciente, con interesados en alquilar el inmueble. La LOCADORA quedará
facultada a rescindir unilateralmente el presente por incumplimiento de la LOCATARIA de cualquiera de
las cláusulas de este contrato.
DECIMO SEPTIMA - ENTREGA DE LLAVES: Dentro de los 30 (treinta) días anteriores al vencimiento o
rescisión del contrato, y 15 (quince) días antes de la entrega de llaves, por cualquiera de los motivos
previstos por Ley, La LOCATARIA deberá comunicar en forma fehaciente a la LOCADORA fecha y hora a
los fines de que esta ultima constate el estado del inmueble, el que será reflejado y suscripto por
ambas partes al momento de recepción del inmueble. Se deja constancia que mas allá de la recepción
de llaves, la LOCATARIA será responsable por los daños y perjuicios que se provoquen a la LOCADORA
por el mal estado del inmueble al momento de la recepción de llaves. Formara parte de este daño,
el
4
lucro cesante (alquileres dejados de percibir, expensas e impuestos devengados durante el plazo de
reparación) causado a la LOCADORA derivado de la demora en realizar las mejoras necesarias en el
inmueble con el fin de restituir este al estado en el que fue entregado al momento de suscribirse
el
presente contrato y la multa indemnizatoria expresada ut supra en la clausula decimo segunda.
DECIMO OCTAVA - ADMINISTRACION: La LOCADORA designa mediante el presente al Sr. SERGIO
AUADA DNI 17.625.554.-, Matrícula 04 - 3592 con domicilio comercial en calle Arturo M. Bas N°
43 Planta Baja Dpto. "1" de ésta ciudad, ADMINISTRADOR del inmueble motivo de este contrato,
facultándolo/a a efectuar la cobranza de los alquileres, recargos por mora, etc., y a extender los
recibos pertinentes; a realizar reparaciones menores a los fines del mejor mantenimiento del
inmueble; a efectuar la entrega y recepción de las llaves; a suscribir la resolución del contrato;
a
efectuar las gestiones necesarias para prorrogar y/o confeccionar un nuevo contrato, a partir de los
noventa días previos al vencimiento del presente contrato; a enviar en nombre y representación de la
LOCADORA las notificaciones fehacientes necesarias; a representarla ante la Municipalidad; D.G.R.;
A.F.I.P.; Aguas Cordobesas; E.P.E.C.; ECOGAS; Telecom y cualquier otra repartición o empresa que
pueda tener algún tipo de relación con el inmueble motivo de este contrato. Queda autorizado/a para
gestionar en su nombre pagos o planes de regularización de deudas de impuestos y servicios, trámites
relacionados con reintegros por doble pago efectuado o para que se acrediten esas sumas a futuros
pagos, presentando y firmando las notas correspondientes; queda facultado/a para solicitar el corte de
suministro de energía eléctrica y de gas natural de las empresas pertinentes como así también para
solicitar ante las mismas las conexiones o reconexiones de dichos servicios. Asimismo las partes
intervinientes facultan al Administrador/a para que por intermedio de abono remita al sistema de
listado de morosidad los antecedentes de todos los integrantes del contrato, en el supuesto de falta de
pago de los alquileres y/o cualquiera de las obligaciones contraídas en el presente contrato. Una vez
regularizada la deuda, la LOCADORA y/o quien la representa harán saber tal situación a la EDITORA, a
los fines de la eliminación de lo acordado en la presente cláusula. Las partes abonarán al matriculado/a
sus honorarios profesionales: la LOCATARIA el correspondiente a la intermediación según ley 7191 y
la
LOCADORA el porcentaje pactado por el cobro mensual de los valores locativos.
DECIMO NOVENA - JURISDICCION: A todos los efectos legales las partes, se someten a la jurisdicción
de los Tribunales Ordinarios de la Ciudad de Córdoba, con renuncia expresa a cualquier otro fuero
o
jurisdicción; la LOCADORA constituye domicilio especial en calle Arturo M. Bas 43 PB 1, Córdoba; y en
segunda instancia fijando domicilio electrónico fernandoauada@gmail.com; la LOCATARIA constituye
domicilio especial en el inmueble que por este acto alquila, y domicilio
electrónico
cande.mui99@gmail.com, y para el caso de desalojo o abandono o restitución del inmueble locado o
consignación judicial de llaves, o cuando sea imposible notificarla al domicilio precedentemente
constituido, la LOCATARIA, fija domicilio de pleno derecho, en calle Duarte Quiros N° 433 C - B°
Centro (CP. 5000), Córdoba; y en segunda instancia fijando domicilio electrónico
emma.mini@hotmail.es y orlamui@hotmail.com, a todos los fines contractuales, judiciales y/o
extrajudiciales debiendo comunicar en forma fehaciente a la LOCADORA cualquier cambio en estos
domicilios; y c) las GARANTIAS en los establecidos en la CLAUSULA DECIMO TERCERA.
DE CONFORMIDAD: Las partes suscriben TRES (3) ejemplares de un mismo tenor y a un solo efecto en
la Ciudad de Córdoba a los veintiocho días del mes de junio de 2022.
Locadora
Locataria
Garantía
Garantía
5"""
lines = documento2.splitlines()
direcciones = []
direccionesTruncado = []     
numero = 0
for line in lines:
    # check if string present on a current line
    if line.find("Calle") != -1:
        #print("Calle", 'está en el texto')
        #print('Número de línea:', lines.index(line))
        direccion = [line, lines[lines.index(line)]]
        #print('Texto:', line, lines[lines.index(line)])
    elif line.find("calle") != -1:
        numero += 1
        #print("calle", 'está en el texto')
        #print('Número de línea:', lines.index(line))
        direcciones.append((str(numero),line, lines[lines.index(line)]))
        #print('Texto:',line, lines[lines.index(line)] )

caracteresMontos= ['Precio', 'precio','comision']
montosTruncados =[]
posicionMonto = 0
subCadenaMonto=""
for direccion in direcciones:
    for linea in direccion:
        subcadena = "calle"
        subcadena2 = "Calle"
        posicion = linea.find(subcadena)
        posicion2 = linea.find(subcadena2)
        if posicion != -1:
            posicion= posicion+5
            direccionesTruncado.append(linea[posicion:])
        elif posicion2 != -1:
            posicion2= posicion2+5
            direccionesTruncado.append(linea[posicion2:])
        elif any((x:=subCadenaMonto) in linea for subCadenaMonto in caracteresMontos):
            posicionMonto= linea.find(x) 
            
   

#nombres = re.findall(r'(?:Sr\.|Sra\.) [a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+', documento2)
print(direcciones)
print(direccionesTruncado)


