class QResponseEnum:
    NOT_AVAILABLE = 0
    YES = 1
    NO = 2
    LOW = 3
    NORMAL = 4
    ABNORMAL = 5
    HIGH = 6
    MILD = 7
    MODERATE = 8
    SEVERE = 9
    BORDERLINE_HIGH = 10
    TY = 11
    YA = 12
    MA = 13
    OA = 14
    STAGE_1 = 15
    STAGE_2 = 16
    STAGE_3 = 17
    STAGE_4 = 18
    D_PENICILLAMINE = 19
    PLACEBO = 20
    MALE = 21
    FEMALE = 22
    ENDEMA_Y = 23
    ENDEMA_N = 24
    ENDEMA_S = 25

# QResponseEnum alias
__QRE = QResponseEnum

# attr_id|text
__response_map = {
    __QRE.NOT_AVAILABLE: ("na", "Not Available"),
    __QRE.YES: ("y", "Yes"),
    __QRE.NO: ("n", "No"),
    __QRE.LOW: ("low", "Low"),
    __QRE.NORMAL: ("normal", "Normal"),
    __QRE.ABNORMAL: ("abnormal", "Abnormal"),
    __QRE.HIGH: ("high", "High"),
    __QRE.MILD: ("mild", "Mild"),
    __QRE.MODERATE: ("moderate", "Moderate"),
    __QRE.SEVERE: ("severe", "Severe"),
    __QRE.BORDERLINE_HIGH: ("borderline high", "Borderline High"),
    __QRE.TY: ("ty", "Teen Years"),
    __QRE.YA: ("ya", "Young Adults"),
    __QRE.MA: ("na", "Middle Age"),
    __QRE.OA: ("oa", "Older Adulthood"),
    __QRE.STAGE_1: ("stage 1", "Stage 1"),
    __QRE.STAGE_2: ("stage 2", "Stage 2"),
    __QRE.STAGE_3: ("stage 3", "Stage 3"),
    __QRE.STAGE_4: ("stage 4", "Stage 4"),
    __QRE.D_PENICILLAMINE: ("d-penicillamine", "D-Penicillamine"),
    __QRE.PLACEBO: ("placebo", "Placebo"),
    __QRE.MALE: ("m", "Male"),
    __QRE.FEMALE: ("f", "Female"),
    __QRE.ENDEMA_Y: ("y", "Edema despite diuretic theraphy"),
    __QRE.ENDEMA_N: ("n", "No Edema and no diuretic therapy for Edema"),
    __QRE.ENDEMA_S: ("s", "With Edema without diuretics or Edema resolved with diuretics"),
}

def response_to_text(response_id):
    return __response_map[response_id][1]

def response_to_attr_id(response_id):
    return __response_map[response_id][0]
