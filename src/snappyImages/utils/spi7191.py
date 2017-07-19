ADC_CS = 28 # connected to SN171 GPIO15
ADC_CS_ACTIVE = False
ADC_CS_NOT_ACTIVE = True
OUTPUT_PIN = True

def snappySpiInit():
    spiInit(
    True,   #Clock Polarity CLOCK IS NORMALLY HIGH
    True,   #Clock Phase    DATA TRIGGERED WHEN CLOCK GOES HIGH
    True,   #Bit Order      SEND MSB FIRST
    False   #3-Wire         ONLY CLK, MISO, MOSI(Not connected), AND GROUND
    )
    setPinDir(ADC_CS, OUTPUT_PIN)
    snappyADCDisable()

def snappySpiRead(bytes, bits_in_last_byte):
    return spiRead(bytes, bits_in_last_byte)

def snappyADCEnable():
    writePin(ADC_CS, ADC_CS_ACTIVE)

def snappyADCDisable():
    writePin(ADC_CS, ADC_CS_NOT_ACTIVE)
