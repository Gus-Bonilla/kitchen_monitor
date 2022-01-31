import threading
import tkinter as tk
import time
from tkinter import ttk
from tkinter.font import Font
# import RPi.GPIO as GPIO
import datetime
from PIL import Image, ImageTk
import PIL
import cv2


class Application(ttk.Frame):
    pin_sound_alarm = 17
    pin_btn = 10
    pin_gas_sensor = 4
    pin_presence_sensor = 27
    pin_temperature_sensor = 22
    alarm_status = False
    width, height = 200, 200
    cap = cv2.VideoCapture(0)
    camera_status = False

    def show_frame(self):
        if self.camera_status:
            _, frame = self.cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img_camera = PIL.Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img_camera)
            self.imgCamera.imgtk = imgtk
            self.imgCamera.configure(image=imgtk)
            self.imgCamera.after(10, self.show_frame)

    def deactivate_alarm(self):
        if self.alarm_status:
            self.alarm_status = False
            self.txtLastEvent.config(background="green")
            self.ledAlarmStatus.config(background="gray")
            self.alarmStatus.set("ALARMA INACTIVA")
            # GPIO.output(self.pin_sound_alarm, False)

    def activate_alarm(self):
        self.txtLastEvent.config(background="red")
        self.ledAlarmStatus.config(background="red")
        self.alarmStatus.set("ALARMA ACTIVA")
        self.alarm_status = True
        # if self.alarmSoundStatus.get():
            # GPIO.output(self.pin_sound_alarm, True)

    def change_button(self, status):
        if status:
            self.ledButton.config(background="red")
        else:
            self.ledButton.config(background="gray")

    def change_gas(self, status):
        if status:
            self.ledSensorGas.config(background="red")
        else:
            self.ledSensorGas.config(background="gray")

    def change_presence(self, status):
        if status:
            self.ledSensorPresence.config(background="red")
        else:
            self.ledSensorPresence.config(background="gray")

    def change_temperature(self, status):
        if status:
            self.ledSensorTemperature.config(background="red")
        else:
            self.ledSensorTemperature.config(background="gray")

    def change_camera_status(self):
        self.camera_status = not self.camera_status
        if self.camera_status:
            self.show_frame()
            self.btnChangeCameraStatus.config(text="INHABILITAR CAMARA")
        else:
            self.imgCamera.configure(image=self.imgDefault)
            self.btnChangeCameraStatus.config(text="HABILITAR CAMARA")

    def read_sensors(self):
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.pin_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.pin_gas_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.pin_presence_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.pin_temperature_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.pin_sound_alarm, GPIO.OUT)
        sensors = [10, 4, 27, 22]
        control_buttons = [2, 3, 9]
        # sensors_status = [GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH]
        # control_status = [GPIO.HIGH, GPIO.HIGH, GPIO.HIGH]
        sensors_names = ["BOTÓN DE EMERGENCIA", "SENSOR DE HUMO Y GAS",
                         "SENSOR DE PRESENCIA", "SENSOR DE CALOR",
                         "NO HAY SENSORES ACTIVOS"]
        sensors_imgs = [self.imgButton, self.imgSensorGas, self.imgSensorPresence,
                        self.imgSensorTemperature, self.imgDefault]
        sensor_index = 0
        control_index = 0
        
        try:
            while 1:
                for control_button in control_buttons:
                    control_index = control_buttons.index(control_button)
                    # if GPIO.input(control_button) != control_status[control_index]:
                    #     if control_status[control_index] == GPIO.HIGH:
                    #         control_status[control_index] = GPIO.LOW

                    #         if control_button == 2:
                    #             self.alarmSoundStatus.set(not self.alarmSoundStatus.get())

                    #        elif control_button == 3:
                    #             self.deactivate_alarm()

                    #         elif control_button == 9:
                    #            self.change_camera_status()

                    #     else:
                    #         control_status[control_index] = GPIO.HIGH

                for sensor in sensors:
                    sensor_index = sensors.index(sensor)
                    # if GPIO.input(sensor) != sensors_status[sensor_index]:                  # Un sensor cambió de estado?
                    #     status = False

                    #     if sensors_status[sensor_index] == GPIO.HIGH:                       # Se ha activado un sensor?
                    #         sensors_status[sensor_index] = GPIO.LOW
                    #         self.activate_alarm()
                    #         status = True
                    #         msg = sensors_names[sensor_index]
                    #         msg += "\n"
                    #         msg += datetime.datetime.now().strftime("%d/%B/%Y, %I:%M%p")
                    #         msg += "\n\n"
                    #         self.txtLogArea.insert("1.0", msg)
                    #         self.lastEvent.set(sensors_names[sensor_index])
                    #         self.lblLastEvent.config(image=sensors_imgs[sensor_index])

                    #     else:                                                               # Se ha desactivado un sensor?
                    #         sensors_status[sensor_index] = GPIO.HIGH
                    #         next_sensor_index = 4

                    #         if GPIO.LOW in sensors_status:
                    #             next_sensor_index = sensors_status.index(GPIO.LOW)

                    #         self.lblLastEvent.config(image=sensors_imgs[next_sensor_index])
                    #         self.lastEvent.set(sensors_names[next_sensor_index])

                    #    if sensor == 10:
                    #         self.change_button(status)

                    #    elif sensor == 4:
                    #         self.change_gas(status)
                        
                    #     elif sensor == 27:
                    #         self.change_presence(status)
                        
                    #     elif sensor == 22:
                    #         self.change_temperature(status)

                time.sleep(0.3)

        finally:
            print("Algo cambió xD")

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("APP")
        main_window.columnconfigure(0, weight=1)
        main_window.rowconfigure(0, weight=1)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        self.imgDefault = tk.PhotoImage(file="Default.png")
        self.imgSensorTemperature = tk.PhotoImage(file="Sensor de fuego o calor.png")
        self.imgSensorTemperatureSmall = self.imgSensorTemperature.subsample(3)
        self.imgSensorPresence = tk.PhotoImage(file="Sensor de presencia.png")
        self.imgSensorPresenceSmall = self.imgSensorPresence.subsample(3)
        self.imgSensorGas = tk.PhotoImage(file="Sensor de humo o gas.png")
        self.imgSensorGasSmall = self.imgSensorGas.subsample(3)
        self.imgButton = tk.PhotoImage(file="Botón de timbre.png")
        self.imgButtonSmall = self.imgButton.subsample(3)

        self.fontStyleBig = Font(family="Lucida Grande", size=16)

        ################################################################################################################
        self.lastEvent = tk.StringVar()                                                     # TXT LAST EVENT
        self.lastEvent.set("NO HAY SENSORES ACTIVOS")
        self.txtLastEvent = tk.Label(self, textvariable=self.lastEvent,
                                      font=self.fontStyleBig, bg="green")
        self.txtLastEvent.grid(row=0, column=0, rowspan=4, columnspan=2)

        self.lblLastEvent = ttk.Label(self, image=self.imgDefault)                          # IMG LAST EVENT
        self.lblLastEvent.grid(row=4, column=0, rowspan=8, columnspan=2)

        self.lblSensorTemperature = ttk.Label(self, image=self.imgSensorTemperatureSmall)   # IMG SENSOR TEMPERATURE
        self.lblSensorTemperature.grid(row=12, column=0, rowspan=2, columnspan=1)

        self.lblSensorPresence = ttk.Label(self, image=self.imgSensorPresenceSmall)         # IMG SENSOR PRESENCE
        self.lblSensorPresence.grid(row=12, column=1, rowspan=2, columnspan=1)

        self.lblSensorGas = ttk.Label(self, image=self.imgSensorGasSmall)                   # IMG SENSOR GAS
        self.lblSensorGas.grid(row=16, column=0, rowspan=2, columnspan=1)

        self.lblButton = ttk.Label(self, image=self.imgButtonSmall)                         # IMG BUTTON
        self.lblButton.grid(row=16, column=1, rowspan=2, columnspan=1)

        self.ledSensorTemperature = tk.Label(self, height=1, width=10, bg="gray")           # LED SENSOR TEMPERATURE
        self.ledSensorTemperature.grid(row=14, column=0, rowspan=1, columnspan=1)

        self.ledSensorPresence = tk.Label(self, height=1, width=10, bg="gray")              # LED SENSOR PRESENCE
        self.ledSensorPresence.grid(row=14, column=1, rowspan=1, columnspan=1)

        self.ledSensorGas = tk.Label(self, height=1, width=10, bg="gray")                   # LED SENSOR GAS
        self.ledSensorGas.grid(row=18, column=0, rowspan=1, columnspan=1)

        self.ledButton = tk.Label(self, height=1, width=10, bg="gray")                      # LED BUTTON
        self.ledButton.grid(row=18, column=1, rowspan=1, columnspan=1)

        self.txtSensorTemperature = ttk.Label(self, text="SENSOR DE CALOR")                 # TXT SENSOR TEMPERATURE
        self.txtSensorTemperature.grid(row=15, column=0, rowspan=1, columnspan=1)

        self.txtSensorPresence = ttk.Label(self, text="SENSOR DE PRESENCIA")                # TXT SENSOR PRESENCE
        self.txtSensorPresence.grid(row=15, column=1, rowspan=1, columnspan=1)

        self.txtSensorGas = ttk.Label(self, text="SENSOR DE HUMO Y GAS")                    # TXT SENSOR GAS
        self.txtSensorGas.grid(row=19, column=0, rowspan=1, columnspan=1)

        self.txtButton = ttk.Label(self, text="BOTÓN DE EMERGENCIA")                        # TXT BUTTON
        self.txtButton.grid(row=19, column=1, rowspan=1, columnspan=1)

        self.txtLogArea = tk.Text(self, relief=tk.RAISED, height=30, width=25,              # TXT LOG AREA
                                  yscrollcommand=True)
        self.txtLogArea.bind("<Key>", lambda e: "break")
        self.txtLogArea.grid(row=4, column=2, rowspan=12, columnspan=3)

        self.btnDeactivateAlarm = tk.Button(self, text="DESACTIVAR ALARMA",                 # BTN DEACTIVATE ALARM
                                            activebackground="green",
                                            command=self.deactivate_alarm)
        self.btnDeactivateAlarm.grid(row=16, column=2, rowspan=4, columnspan=3)

        self.imgCamera = tk.Label(self, image=self.imgDefault)                  # IMG CAMERA [, height=320, width=240]
        self.imgCamera.grid(row=0, column=5, rowspan=12, columnspan=1)

        self.btnChangeCameraStatus = ttk.Button(self, text="HABILITAR CAMARA",              # BTN CHANGE CAMERA STATUS
                                                command=self.change_camera_status)
        self.btnChangeCameraStatus.grid(row=12, column=5, rowspan=1, columnspan=1)

        self.alarmStatus = tk.StringVar()                                                   # TXT ALARM STATUS
        self.alarmStatus.set("ALARMA INACTIVA")
        self.txtAlarmStatus = ttk.Label(self, textvar=self.alarmStatus)
        self.txtAlarmStatus.grid(row=14, column=5, rowspan=1, columnspan=1)

        self.ledAlarmStatus = tk.Label(self, height=1, width=50, bg="gray")                 # LED ALARM STATUS
        self.ledAlarmStatus.grid(row=15, column=5, rowspan=1, columnspan=1)

        self.alarmSoundStatus = tk.BooleanVar()                                             # CHECKBUTTON ALARM SOUND
        self.cbtnAlarmSound = tk.Checkbutton(self, text="SONIDO EN ALARMA",
                                             variable=self.alarmSoundStatus,
                                             onvalue=True, offvalue=False)
        self.alarmSoundStatus.set(True)
        self.cbtnAlarmSound.grid(row=16, column=5, rowspan=4, columnspan=1)

        ################################################################################################################

        self.grid(sticky="nsew")


window = tk.Tk()
app = Application(window)
sensors_task = threading.Thread(target=app.read_sensors, daemon=True)
sensors_task.start()
app.show_frame()
app.mainloop()
