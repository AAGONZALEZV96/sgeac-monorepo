from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

_boolean = bool
_double = float
_doubleMin0 = float
_doubleMin0Max1 = float
_doubleMin0Max2147483647 = float
_doubleMin1Max10 = float
_doubleMinNegative59Max0 = float
_doubleMinNegative60Max3 = float
_doubleMinNegative60Max6 = float
_doubleMinNegative60MaxNegative1 = float
_doubleMinNegative6Max3 = float
_doubleMinNegative8Max0 = float
_integer = int
_integerMin0Max0 = int
_integerMin0Max1 = int
_integerMin0Max10 = int
_integerMin0Max100 = int
_integerMin0Max1000 = int
_integerMin0Max10000 = int
_integerMin0Max1152000000 = int
_integerMin0Max128 = int
_integerMin0Max1466400000 = int
_integerMin0Max15 = int
_integerMin0Max16 = int
_integerMin0Max2147483647 = int
_integerMin0Max255 = int
_integerMin0Max3 = int
_integerMin0Max30 = int
_integerMin0Max30000 = int
_integerMin0Max3600 = int
_integerMin0Max4 = int
_integerMin0Max4000 = int
_integerMin0Max4194303 = int
_integerMin0Max47185920 = int
_integerMin0Max5 = int
_integerMin0Max500 = int
_integerMin0Max50000 = int
_integerMin0Max65534 = int
_integerMin0Max65535 = int
_integerMin0Max7 = int
_integerMin0Max8 = int
_integerMin0Max9 = int
_integerMin0Max96 = int
_integerMin0Max99 = int
_integerMin100000Max100000000 = int
_integerMin1000Max1152000000 = int
_integerMin1000Max1466400000 = int
_integerMin1000Max288000000 = int
_integerMin1000Max30000 = int
_integerMin1000Max300000000 = int
_integerMin1000Max480000000 = int
_integerMin100Max1000 = int
_integerMin10Max48 = int
_integerMin16000Max320000 = int
_integerMin16000Max48000 = int
_integerMin16Max24 = int
_integerMin1Max1 = int
_integerMin1Max10 = int
_integerMin1Max100 = int
_integerMin1Max10000000 = int
_integerMin1Max1001 = int
_integerMin1Max150 = int
_integerMin1Max17895697 = int
_integerMin1Max2 = int
_integerMin1Max20 = int
_integerMin1Max2048 = int
_integerMin1Max2147483640 = int
_integerMin1Max2147483647 = int
_integerMin1Max31 = int
_integerMin1Max32 = int
_integerMin1Max4 = int
_integerMin1Max4096 = int
_integerMin1Max512 = int
_integerMin1Max6 = int
_integerMin1Max60000 = int
_integerMin1Max64 = int
_integerMin1Max8 = int
_integerMin22050Max48000 = int
_integerMin24Max60000 = int
_integerMin25Max10000 = int
_integerMin25Max2000 = int
_integerMin2Max2147483647 = int
_integerMin2Max4096 = int
_integerMin32000Max192000 = int
_integerMin32000Max3024000 = int
_integerMin32000Max384000 = int
_integerMin32000Max48000 = int
_integerMin32Max8182 = int
_integerMin32Max8192 = int
_integerMin384000Max1024000 = int
_integerMin3Max15 = int
_integerMin48000Max48000 = int
_integerMin4Max12 = int
_integerMin50Max86400000 = int
_integerMin6000Max1024000 = int
_integerMin64000Max640000 = int
_integerMin8000Max192000 = int
_integerMin8000Max96000 = int
_integerMin8Max12 = int
_integerMin8Max4096 = int
_integerMin90Max105 = int
_integerMin920Max1023 = int
_integerMin96Max600 = int
_integerMinNegative10000Max10000 = int
_integerMinNegative1000Max1000 = int
_integerMinNegative180Max180 = int
_integerMinNegative1Max10 = int
_integerMinNegative1Max2147483647 = int
_integerMinNegative1Max3 = int
_integerMinNegative2147483648Max2147483647 = int
_integerMinNegative2Max3 = int
_integerMinNegative50Max50 = int
_integerMinNegative5Max10 = int
_integerMinNegative60Max6 = int
_integerMinNegative70Max0 = int
_string = str
_stringMax1000 = str
_stringMax2048 = str
_stringMax2048PatternS3Https = str
_stringMax256 = str
_stringMin0 = str
_stringMin1 = str
_stringMin11Max11Pattern01D20305D205D = str
_stringMin14PatternS3BmpBMPPngPNGHttpsBmpBMPPngPNG = str
_stringMin14PatternS3BmpBMPPngPNGTgaTGAHttpsBmpBMPPngPNGTgaTGA = str
_stringMin14PatternS3CubeCUBEHttpsCubeCUBE = str
_stringMin14PatternS3Mov09PngHttpsMov09Png = str
_stringMin14PatternS3SccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTTHttpsSccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTT = str
_stringMin14PatternS3XmlXMLHttpsXmlXML = str
_stringMin16Max24PatternAZaZ0922AZaZ0916 = str
_stringMin1Max100000 = str
_stringMin1Max20 = str
_stringMin1Max2048PatternArnAZSecretsmanagerWD12SecretAZAZ09 = str
_stringMin1Max256 = str
_stringMin1Max50 = str
_stringMin1Max50PatternAZAZ09 = str
_stringMin24Max512PatternAZaZ0902 = str
_stringMin32Max32Pattern09aFAF32 = str
_stringMin36Max36Pattern09aFAF809aFAF409aFAF409aFAF409aFAF12 = str
_stringMin3Max3Pattern1809aFAF09aEAE = str
_stringMin3Max3PatternAZaZ3 = str
_stringMin6Max8Pattern09aFAF609aFAF2 = str
_stringMin9Max19PatternAZ26EastWestCentralNorthSouthEastWest1912 = str
_stringPattern = str
_stringPattern010920405090509092 = str
_stringPattern010920405090509092090909 = str
_stringPattern01D20305D205D = str
_stringPattern0940191020191209301 = str
_stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12 = str
_stringPattern0xAFaF0908190908 = str
_stringPatternAZaZ0902 = str
_stringPatternAZaZ0932 = str
_stringPatternAZaZ23AZaZ = str
_stringPatternAZaZ23AZaZ09 = str
_stringPatternArnAwsUsGovAcm = str
_stringPatternArnAwsUsGovCnKmsAZ26EastWestCentralNorthSouthEastWest1912D12KeyAFAF098AFAF094AFAF094AFAF094AFAF0912MrkAFAF0932 = str
_stringPatternDD = str
_stringPatternHttps = str
_stringPatternHttpsD = str
_stringPatternHttpsKantarmedia = str
_stringPatternIdentityAZaZ26AZaZ09163 = str
_stringPatternS3 = str
_stringPatternS3ASSETMAPXml = str
_stringPatternS3Https = str
_stringPatternS3TtfHttpsTtf = str
_stringPatternSNManifestConfirmConditionNotificationNS = str
_stringPatternSNSignalProcessingNotificationNS = str
_stringPatternW = str
_stringPatternWS = str


class AacAudioDescriptionBroadcasterMix(StrEnum):
    BROADCASTER_MIXED_AD = "BROADCASTER_MIXED_AD"
    NORMAL = "NORMAL"


class AacCodecProfile(StrEnum):
    LC = "LC"
    HEV1 = "HEV1"
    HEV2 = "HEV2"


class AacCodingMode(StrEnum):
    AD_RECEIVER_MIX = "AD_RECEIVER_MIX"
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_5_1 = "CODING_MODE_5_1"


class AacRateControlMode(StrEnum):
    CBR = "CBR"
    VBR = "VBR"


class AacRawFormat(StrEnum):
    LATM_LOAS = "LATM_LOAS"
    NONE = "NONE"


class AacSpecification(StrEnum):
    MPEG2 = "MPEG2"
    MPEG4 = "MPEG4"


class AacVbrQuality(StrEnum):
    LOW = "LOW"
    MEDIUM_LOW = "MEDIUM_LOW"
    MEDIUM_HIGH = "MEDIUM_HIGH"
    HIGH = "HIGH"


class Ac3BitstreamMode(StrEnum):
    COMPLETE_MAIN = "COMPLETE_MAIN"
    COMMENTARY = "COMMENTARY"
    DIALOGUE = "DIALOGUE"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    MUSIC_AND_EFFECTS = "MUSIC_AND_EFFECTS"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"
    VOICE_OVER = "VOICE_OVER"


class Ac3CodingMode(StrEnum):
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2_LFE = "CODING_MODE_3_2_LFE"


class Ac3DynamicRangeCompressionLine(StrEnum):
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"
    NONE = "NONE"


class Ac3DynamicRangeCompressionProfile(StrEnum):
    FILM_STANDARD = "FILM_STANDARD"
    NONE = "NONE"


class Ac3DynamicRangeCompressionRf(StrEnum):
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"
    NONE = "NONE"


class Ac3LfeFilter(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Ac3MetadataControl(StrEnum):
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AccelerationMode(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    PREFERRED = "PREFERRED"


class AccelerationStatus(StrEnum):
    NOT_APPLICABLE = "NOT_APPLICABLE"
    IN_PROGRESS = "IN_PROGRESS"
    ACCELERATED = "ACCELERATED"
    NOT_ACCELERATED = "NOT_ACCELERATED"


class AdvancedInputFilter(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AdvancedInputFilterAddTexture(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AdvancedInputFilterSharpen(StrEnum):
    OFF = "OFF"
    LOW = "LOW"
    HIGH = "HIGH"


class AfdSignaling(StrEnum):
    NONE = "NONE"
    AUTO = "AUTO"
    FIXED = "FIXED"


class AlphaBehavior(StrEnum):
    DISCARD = "DISCARD"
    REMAP_TO_LUMA = "REMAP_TO_LUMA"


class AncillaryConvert608To708(StrEnum):
    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


class AncillaryTerminateCaptions(StrEnum):
    END_OF_INPUT = "END_OF_INPUT"
    DISABLED = "DISABLED"


class AntiAlias(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AudioChannelTag(StrEnum):
    L = "L"
    R = "R"
    C = "C"
    LFE = "LFE"
    LS = "LS"
    RS = "RS"
    LC = "LC"
    RC = "RC"
    CS = "CS"
    LSD = "LSD"
    RSD = "RSD"
    TCS = "TCS"
    VHL = "VHL"
    VHC = "VHC"
    VHR = "VHR"
    TBL = "TBL"
    TBC = "TBC"
    TBR = "TBR"
    RSL = "RSL"
    RSR = "RSR"
    LW = "LW"
    RW = "RW"
    LFE2 = "LFE2"
    LT = "LT"
    RT = "RT"
    HI = "HI"
    NAR = "NAR"
    M = "M"


class AudioCodec(StrEnum):
    AAC = "AAC"
    MP2 = "MP2"
    MP3 = "MP3"
    WAV = "WAV"
    AIFF = "AIFF"
    AC3 = "AC3"
    EAC3 = "EAC3"
    EAC3_ATMOS = "EAC3_ATMOS"
    VORBIS = "VORBIS"
    OPUS = "OPUS"
    PASSTHROUGH = "PASSTHROUGH"
    FLAC = "FLAC"


class AudioDefaultSelection(StrEnum):
    DEFAULT = "DEFAULT"
    NOT_DEFAULT = "NOT_DEFAULT"


class AudioDurationCorrection(StrEnum):
    DISABLED = "DISABLED"
    AUTO = "AUTO"
    TRACK = "TRACK"
    FRAME = "FRAME"
    FORCE = "FORCE"


class AudioLanguageCodeControl(StrEnum):
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AudioNormalizationAlgorithm(StrEnum):
    ITU_BS_1770_1 = "ITU_BS_1770_1"
    ITU_BS_1770_2 = "ITU_BS_1770_2"
    ITU_BS_1770_3 = "ITU_BS_1770_3"
    ITU_BS_1770_4 = "ITU_BS_1770_4"


class AudioNormalizationAlgorithmControl(StrEnum):
    CORRECT_AUDIO = "CORRECT_AUDIO"
    MEASURE_ONLY = "MEASURE_ONLY"


class AudioNormalizationLoudnessLogging(StrEnum):
    LOG = "LOG"
    DONT_LOG = "DONT_LOG"


class AudioNormalizationPeakCalculation(StrEnum):
    TRUE_PEAK = "TRUE_PEAK"
    NONE = "NONE"


class AudioSelectorType(StrEnum):
    PID = "PID"
    TRACK = "TRACK"
    LANGUAGE_CODE = "LANGUAGE_CODE"
    HLS_RENDITION_GROUP = "HLS_RENDITION_GROUP"
    ALL_PCM = "ALL_PCM"


class AudioTypeControl(StrEnum):
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class Av1AdaptiveQuantization(StrEnum):
    OFF = "OFF"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"


class Av1BitDepth(StrEnum):
    BIT_8 = "BIT_8"
    BIT_10 = "BIT_10"


class Av1FilmGrainSynthesis(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Av1FramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Av1FramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Av1RateControlMode(StrEnum):
    QVBR = "QVBR"


class Av1SpatialAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AvcIntraClass(StrEnum):
    CLASS_50 = "CLASS_50"
    CLASS_100 = "CLASS_100"
    CLASS_200 = "CLASS_200"
    CLASS_4K_2K = "CLASS_4K_2K"


class AvcIntraFramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class AvcIntraFramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class AvcIntraInterlaceMode(StrEnum):
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class AvcIntraScanTypeConversionMode(StrEnum):
    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class AvcIntraSlowPal(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AvcIntraTelecine(StrEnum):
    NONE = "NONE"
    HARD = "HARD"


class AvcIntraUhdQualityTuningLevel(StrEnum):
    SINGLE_PASS = "SINGLE_PASS"
    MULTI_PASS = "MULTI_PASS"


class BandwidthReductionFilterSharpening(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    OFF = "OFF"


class BandwidthReductionFilterStrength(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    AUTO = "AUTO"
    OFF = "OFF"


class BillingTagsSource(StrEnum):
    QUEUE = "QUEUE"
    PRESET = "PRESET"
    JOB_TEMPLATE = "JOB_TEMPLATE"
    JOB = "JOB"


class BurnInSubtitleStylePassthrough(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class BurninSubtitleAlignment(StrEnum):
    CENTERED = "CENTERED"
    LEFT = "LEFT"
    AUTO = "AUTO"


class BurninSubtitleApplyFontColor(StrEnum):
    WHITE_TEXT_ONLY = "WHITE_TEXT_ONLY"
    ALL_TEXT = "ALL_TEXT"


class BurninSubtitleBackgroundColor(StrEnum):
    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    AUTO = "AUTO"


class BurninSubtitleFallbackFont(StrEnum):
    BEST_MATCH = "BEST_MATCH"
    MONOSPACED_SANSSERIF = "MONOSPACED_SANSSERIF"
    MONOSPACED_SERIF = "MONOSPACED_SERIF"
    PROPORTIONAL_SANSSERIF = "PROPORTIONAL_SANSSERIF"
    PROPORTIONAL_SERIF = "PROPORTIONAL_SERIF"


class BurninSubtitleFontColor(StrEnum):
    WHITE = "WHITE"
    BLACK = "BLACK"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    HEX = "HEX"
    AUTO = "AUTO"


class BurninSubtitleOutlineColor(StrEnum):
    BLACK = "BLACK"
    WHITE = "WHITE"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    AUTO = "AUTO"


class BurninSubtitleShadowColor(StrEnum):
    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    AUTO = "AUTO"


class BurninSubtitleTeletextSpacing(StrEnum):
    FIXED_GRID = "FIXED_GRID"
    PROPORTIONAL = "PROPORTIONAL"
    AUTO = "AUTO"


class CaptionDestinationType(StrEnum):
    BURN_IN = "BURN_IN"
    DVB_SUB = "DVB_SUB"
    EMBEDDED = "EMBEDDED"
    EMBEDDED_PLUS_SCTE20 = "EMBEDDED_PLUS_SCTE20"
    IMSC = "IMSC"
    SCTE20_PLUS_EMBEDDED = "SCTE20_PLUS_EMBEDDED"
    SCC = "SCC"
    SRT = "SRT"
    SMI = "SMI"
    TELETEXT = "TELETEXT"
    TTML = "TTML"
    WEBVTT = "WEBVTT"


class CaptionSourceByteRateLimit(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CaptionSourceConvertPaintOnToPopOn(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CaptionSourceType(StrEnum):
    ANCILLARY = "ANCILLARY"
    DVB_SUB = "DVB_SUB"
    EMBEDDED = "EMBEDDED"
    SCTE20 = "SCTE20"
    SCC = "SCC"
    TTML = "TTML"
    STL = "STL"
    SRT = "SRT"
    SMI = "SMI"
    SMPTE_TT = "SMPTE_TT"
    TELETEXT = "TELETEXT"
    NULL_SOURCE = "NULL_SOURCE"
    IMSC = "IMSC"
    WEBVTT = "WEBVTT"


class CaptionSourceUpconvertSTLToTeletext(StrEnum):
    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


class ChromaPositionMode(StrEnum):
    AUTO = "AUTO"
    FORCE_CENTER = "FORCE_CENTER"
    FORCE_TOP_LEFT = "FORCE_TOP_LEFT"


class CmafClientCache(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CmafCodecSpecification(StrEnum):
    RFC_6381 = "RFC_6381"
    RFC_4281 = "RFC_4281"


class CmafEncryptionType(StrEnum):
    SAMPLE_AES = "SAMPLE_AES"
    AES_CTR = "AES_CTR"


class CmafImageBasedTrickPlay(StrEnum):
    NONE = "NONE"
    THUMBNAIL = "THUMBNAIL"
    THUMBNAIL_AND_FULLFRAME = "THUMBNAIL_AND_FULLFRAME"
    ADVANCED = "ADVANCED"


class CmafInitializationVectorInManifest(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class CmafIntervalCadence(StrEnum):
    FOLLOW_IFRAME = "FOLLOW_IFRAME"
    FOLLOW_CUSTOM = "FOLLOW_CUSTOM"


class CmafKeyProviderType(StrEnum):
    SPEKE = "SPEKE"
    STATIC_KEY = "STATIC_KEY"


class CmafManifestCompression(StrEnum):
    GZIP = "GZIP"
    NONE = "NONE"


class CmafManifestDurationFormat(StrEnum):
    FLOATING_POINT = "FLOATING_POINT"
    INTEGER = "INTEGER"


class CmafMpdManifestBandwidthType(StrEnum):
    AVERAGE = "AVERAGE"
    MAX = "MAX"


class CmafMpdProfile(StrEnum):
    MAIN_PROFILE = "MAIN_PROFILE"
    ON_DEMAND_PROFILE = "ON_DEMAND_PROFILE"


class CmafPtsOffsetHandlingForBFrames(StrEnum):
    ZERO_BASED = "ZERO_BASED"
    MATCH_INITIAL_PTS = "MATCH_INITIAL_PTS"


class CmafSegmentControl(StrEnum):
    SINGLE_FILE = "SINGLE_FILE"
    SEGMENTED_FILES = "SEGMENTED_FILES"


class CmafSegmentLengthControl(StrEnum):
    EXACT = "EXACT"
    GOP_MULTIPLE = "GOP_MULTIPLE"
    MATCH = "MATCH"


class CmafStreamInfResolution(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class CmafTargetDurationCompatibilityMode(StrEnum):
    LEGACY = "LEGACY"
    SPEC_COMPLIANT = "SPEC_COMPLIANT"


class CmafVideoCompositionOffsets(StrEnum):
    SIGNED = "SIGNED"
    UNSIGNED = "UNSIGNED"


class CmafWriteDASHManifest(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CmafWriteHLSManifest(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CmafWriteSegmentTimelineInRepresentation(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CmfcAudioDuration(StrEnum):
    DEFAULT_CODEC_DURATION = "DEFAULT_CODEC_DURATION"
    MATCH_VIDEO_DURATION = "MATCH_VIDEO_DURATION"


class CmfcAudioTrackType(StrEnum):
    ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT = "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT"
    ALTERNATE_AUDIO_AUTO_SELECT = "ALTERNATE_AUDIO_AUTO_SELECT"
    ALTERNATE_AUDIO_NOT_AUTO_SELECT = "ALTERNATE_AUDIO_NOT_AUTO_SELECT"
    AUDIO_ONLY_VARIANT_STREAM = "AUDIO_ONLY_VARIANT_STREAM"


class CmfcDescriptiveVideoServiceFlag(StrEnum):
    DONT_FLAG = "DONT_FLAG"
    FLAG = "FLAG"


class CmfcIFrameOnlyManifest(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class CmfcKlvMetadata(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class CmfcManifestMetadataSignaling(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CmfcScte35Esam(StrEnum):
    INSERT = "INSERT"
    NONE = "NONE"


class CmfcScte35Source(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class CmfcTimedMetadata(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class CmfcTimedMetadataBoxVersion(StrEnum):
    VERSION_0 = "VERSION_0"
    VERSION_1 = "VERSION_1"


class Codec(StrEnum):
    UNKNOWN = "UNKNOWN"
    AAC = "AAC"
    AC3 = "AC3"
    EAC3 = "EAC3"
    FLAC = "FLAC"
    MP3 = "MP3"
    OPUS = "OPUS"
    PCM = "PCM"
    VORBIS = "VORBIS"
    AV1 = "AV1"
    AVC = "AVC"
    HEVC = "HEVC"
    MJPEG = "MJPEG"
    MP4V = "MP4V"
    MPEG2 = "MPEG2"
    PRORES = "PRORES"
    THEORA = "THEORA"
    VP8 = "VP8"
    VP9 = "VP9"
    C608 = "C608"
    C708 = "C708"
    WEBVTT = "WEBVTT"


class ColorMetadata(StrEnum):
    IGNORE = "IGNORE"
    INSERT = "INSERT"


class ColorPrimaries(StrEnum):
    ITU_709 = "ITU_709"
    UNSPECIFIED = "UNSPECIFIED"
    RESERVED = "RESERVED"
    ITU_470M = "ITU_470M"
    ITU_470BG = "ITU_470BG"
    SMPTE_170M = "SMPTE_170M"
    SMPTE_240M = "SMPTE_240M"
    GENERIC_FILM = "GENERIC_FILM"
    ITU_2020 = "ITU_2020"
    SMPTE_428_1 = "SMPTE_428_1"
    SMPTE_431_2 = "SMPTE_431_2"
    SMPTE_EG_432_1 = "SMPTE_EG_432_1"
    IPT = "IPT"
    SMPTE_2067XYZ = "SMPTE_2067XYZ"
    EBU_3213_E = "EBU_3213_E"
    LAST = "LAST"


class ColorSpace(StrEnum):
    FOLLOW = "FOLLOW"
    REC_601 = "REC_601"
    REC_709 = "REC_709"
    HDR10 = "HDR10"
    HLG_2020 = "HLG_2020"
    P3DCI = "P3DCI"
    P3D65_SDR = "P3D65_SDR"
    P3D65_HDR = "P3D65_HDR"


class ColorSpaceConversion(StrEnum):
    NONE = "NONE"
    FORCE_601 = "FORCE_601"
    FORCE_709 = "FORCE_709"
    FORCE_HDR10 = "FORCE_HDR10"
    FORCE_HLG_2020 = "FORCE_HLG_2020"
    FORCE_P3DCI = "FORCE_P3DCI"
    FORCE_P3D65_SDR = "FORCE_P3D65_SDR"
    FORCE_P3D65_HDR = "FORCE_P3D65_HDR"


class ColorSpaceUsage(StrEnum):
    FORCE = "FORCE"
    FALLBACK = "FALLBACK"


class Commitment(StrEnum):
    ONE_YEAR = "ONE_YEAR"


class ContainerType(StrEnum):
    F4V = "F4V"
    GIF = "GIF"
    ISMV = "ISMV"
    M2TS = "M2TS"
    M3U8 = "M3U8"
    CMFC = "CMFC"
    MOV = "MOV"
    MP4 = "MP4"
    MPD = "MPD"
    MXF = "MXF"
    OGG = "OGG"
    WEBM = "WEBM"
    RAW = "RAW"
    Y4M = "Y4M"


class CopyProtectionAction(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    STRIP = "STRIP"


class DashIsoGroupAudioChannelConfigSchemeIdUri(StrEnum):
    MPEG_CHANNEL_CONFIGURATION = "MPEG_CHANNEL_CONFIGURATION"
    DOLBY_CHANNEL_CONFIGURATION = "DOLBY_CHANNEL_CONFIGURATION"


class DashIsoHbbtvCompliance(StrEnum):
    HBBTV_1_5 = "HBBTV_1_5"
    NONE = "NONE"


class DashIsoImageBasedTrickPlay(StrEnum):
    NONE = "NONE"
    THUMBNAIL = "THUMBNAIL"
    THUMBNAIL_AND_FULLFRAME = "THUMBNAIL_AND_FULLFRAME"
    ADVANCED = "ADVANCED"


class DashIsoIntervalCadence(StrEnum):
    FOLLOW_IFRAME = "FOLLOW_IFRAME"
    FOLLOW_CUSTOM = "FOLLOW_CUSTOM"


class DashIsoMpdManifestBandwidthType(StrEnum):
    AVERAGE = "AVERAGE"
    MAX = "MAX"


class DashIsoMpdProfile(StrEnum):
    MAIN_PROFILE = "MAIN_PROFILE"
    ON_DEMAND_PROFILE = "ON_DEMAND_PROFILE"


class DashIsoPlaybackDeviceCompatibility(StrEnum):
    CENC_V1 = "CENC_V1"
    UNENCRYPTED_SEI = "UNENCRYPTED_SEI"


class DashIsoPtsOffsetHandlingForBFrames(StrEnum):
    ZERO_BASED = "ZERO_BASED"
    MATCH_INITIAL_PTS = "MATCH_INITIAL_PTS"


class DashIsoSegmentControl(StrEnum):
    SINGLE_FILE = "SINGLE_FILE"
    SEGMENTED_FILES = "SEGMENTED_FILES"


class DashIsoSegmentLengthControl(StrEnum):
    EXACT = "EXACT"
    GOP_MULTIPLE = "GOP_MULTIPLE"
    MATCH = "MATCH"


class DashIsoVideoCompositionOffsets(StrEnum):
    SIGNED = "SIGNED"
    UNSIGNED = "UNSIGNED"


class DashIsoWriteSegmentTimelineInRepresentation(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DashManifestStyle(StrEnum):
    BASIC = "BASIC"
    COMPACT = "COMPACT"
    DISTINCT = "DISTINCT"


class DecryptionMode(StrEnum):
    AES_CTR = "AES_CTR"
    AES_CBC = "AES_CBC"
    AES_GCM = "AES_GCM"


class DeinterlaceAlgorithm(StrEnum):
    INTERPOLATE = "INTERPOLATE"
    INTERPOLATE_TICKER = "INTERPOLATE_TICKER"
    BLEND = "BLEND"
    BLEND_TICKER = "BLEND_TICKER"
    LINEAR_INTERPOLATION = "LINEAR_INTERPOLATION"


class DeinterlacerControl(StrEnum):
    FORCE_ALL_FRAMES = "FORCE_ALL_FRAMES"
    NORMAL = "NORMAL"


class DeinterlacerMode(StrEnum):
    DEINTERLACE = "DEINTERLACE"
    INVERSE_TELECINE = "INVERSE_TELECINE"
    ADAPTIVE = "ADAPTIVE"


class DescribeEndpointsMode(StrEnum):
    DEFAULT = "DEFAULT"
    GET_ONLY = "GET_ONLY"


class DolbyVisionLevel6Mode(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    RECALCULATE = "RECALCULATE"
    SPECIFY = "SPECIFY"


class DolbyVisionMapping(StrEnum):
    HDR10_NOMAP = "HDR10_NOMAP"
    HDR10_1000 = "HDR10_1000"


class DolbyVisionProfile(StrEnum):
    PROFILE_5 = "PROFILE_5"
    PROFILE_8_1 = "PROFILE_8_1"


class DropFrameTimecode(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class DvbSubSubtitleFallbackFont(StrEnum):
    BEST_MATCH = "BEST_MATCH"
    MONOSPACED_SANSSERIF = "MONOSPACED_SANSSERIF"
    MONOSPACED_SERIF = "MONOSPACED_SERIF"
    PROPORTIONAL_SANSSERIF = "PROPORTIONAL_SANSSERIF"
    PROPORTIONAL_SERIF = "PROPORTIONAL_SERIF"


class DvbSubtitleAlignment(StrEnum):
    CENTERED = "CENTERED"
    LEFT = "LEFT"
    AUTO = "AUTO"


class DvbSubtitleApplyFontColor(StrEnum):
    WHITE_TEXT_ONLY = "WHITE_TEXT_ONLY"
    ALL_TEXT = "ALL_TEXT"


class DvbSubtitleBackgroundColor(StrEnum):
    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    AUTO = "AUTO"


class DvbSubtitleFontColor(StrEnum):
    WHITE = "WHITE"
    BLACK = "BLACK"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    HEX = "HEX"
    AUTO = "AUTO"


class DvbSubtitleOutlineColor(StrEnum):
    BLACK = "BLACK"
    WHITE = "WHITE"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    AUTO = "AUTO"


class DvbSubtitleShadowColor(StrEnum):
    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    AUTO = "AUTO"


class DvbSubtitleStylePassthrough(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DvbSubtitleTeletextSpacing(StrEnum):
    FIXED_GRID = "FIXED_GRID"
    PROPORTIONAL = "PROPORTIONAL"
    AUTO = "AUTO"


class DvbSubtitlingType(StrEnum):
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    STANDARD = "STANDARD"


class DvbddsHandling(StrEnum):
    NONE = "NONE"
    SPECIFIED = "SPECIFIED"
    NO_DISPLAY_WINDOW = "NO_DISPLAY_WINDOW"


class DynamicAudioSelectorType(StrEnum):
    ALL_TRACKS = "ALL_TRACKS"
    LANGUAGE_CODE = "LANGUAGE_CODE"


class Eac3AtmosBitstreamMode(StrEnum):
    COMPLETE_MAIN = "COMPLETE_MAIN"


class Eac3AtmosCodingMode(StrEnum):
    CODING_MODE_AUTO = "CODING_MODE_AUTO"
    CODING_MODE_5_1_4 = "CODING_MODE_5_1_4"
    CODING_MODE_7_1_4 = "CODING_MODE_7_1_4"
    CODING_MODE_9_1_6 = "CODING_MODE_9_1_6"


class Eac3AtmosDialogueIntelligence(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3AtmosDownmixControl(StrEnum):
    SPECIFIED = "SPECIFIED"
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"


class Eac3AtmosDynamicRangeCompressionLine(StrEnum):
    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3AtmosDynamicRangeCompressionRf(StrEnum):
    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3AtmosDynamicRangeControl(StrEnum):
    SPECIFIED = "SPECIFIED"
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"


class Eac3AtmosMeteringMode(StrEnum):
    LEQ_A = "LEQ_A"
    ITU_BS_1770_1 = "ITU_BS_1770_1"
    ITU_BS_1770_2 = "ITU_BS_1770_2"
    ITU_BS_1770_3 = "ITU_BS_1770_3"
    ITU_BS_1770_4 = "ITU_BS_1770_4"


class Eac3AtmosStereoDownmix(StrEnum):
    NOT_INDICATED = "NOT_INDICATED"
    STEREO = "STEREO"
    SURROUND = "SURROUND"
    DPL2 = "DPL2"


class Eac3AtmosSurroundExMode(StrEnum):
    NOT_INDICATED = "NOT_INDICATED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3AttenuationControl(StrEnum):
    ATTENUATE_3_DB = "ATTENUATE_3_DB"
    NONE = "NONE"


class Eac3BitstreamMode(StrEnum):
    COMPLETE_MAIN = "COMPLETE_MAIN"
    COMMENTARY = "COMMENTARY"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"


class Eac3CodingMode(StrEnum):
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2 = "CODING_MODE_3_2"


class Eac3DcFilter(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3DynamicRangeCompressionLine(StrEnum):
    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3DynamicRangeCompressionRf(StrEnum):
    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3LfeControl(StrEnum):
    LFE = "LFE"
    NO_LFE = "NO_LFE"


class Eac3LfeFilter(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3MetadataControl(StrEnum):
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class Eac3PassthroughControl(StrEnum):
    WHEN_POSSIBLE = "WHEN_POSSIBLE"
    NO_PASSTHROUGH = "NO_PASSTHROUGH"


class Eac3PhaseControl(StrEnum):
    SHIFT_90_DEGREES = "SHIFT_90_DEGREES"
    NO_SHIFT = "NO_SHIFT"


class Eac3StereoDownmix(StrEnum):
    NOT_INDICATED = "NOT_INDICATED"
    LO_RO = "LO_RO"
    LT_RT = "LT_RT"
    DPL2 = "DPL2"


class Eac3SurroundExMode(StrEnum):
    NOT_INDICATED = "NOT_INDICATED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3SurroundMode(StrEnum):
    NOT_INDICATED = "NOT_INDICATED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EmbeddedConvert608To708(StrEnum):
    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


class EmbeddedTerminateCaptions(StrEnum):
    END_OF_INPUT = "END_OF_INPUT"
    DISABLED = "DISABLED"


class EmbeddedTimecodeOverride(StrEnum):
    NONE = "NONE"
    USE_MDPM = "USE_MDPM"


class F4vMoovPlacement(StrEnum):
    PROGRESSIVE_DOWNLOAD = "PROGRESSIVE_DOWNLOAD"
    NORMAL = "NORMAL"


class FileSourceConvert608To708(StrEnum):
    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


class FileSourceTimeDeltaUnits(StrEnum):
    SECONDS = "SECONDS"
    MILLISECONDS = "MILLISECONDS"


class FontScript(StrEnum):
    AUTOMATIC = "AUTOMATIC"
    HANS = "HANS"
    HANT = "HANT"


class Format(StrEnum):
    mp4 = "mp4"
    quicktime = "quicktime"
    matroska = "matroska"
    webm = "webm"


class FrameMetricType(StrEnum):
    PSNR = "PSNR"
    SSIM = "SSIM"
    MS_SSIM = "MS_SSIM"
    PSNR_HVS = "PSNR_HVS"
    VMAF = "VMAF"
    QVBR = "QVBR"


class GifFramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class GifFramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"


class H264AdaptiveQuantization(StrEnum):
    OFF = "OFF"
    AUTO = "AUTO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"


class H264CodecLevel(StrEnum):
    AUTO = "AUTO"
    LEVEL_1 = "LEVEL_1"
    LEVEL_1_1 = "LEVEL_1_1"
    LEVEL_1_2 = "LEVEL_1_2"
    LEVEL_1_3 = "LEVEL_1_3"
    LEVEL_2 = "LEVEL_2"
    LEVEL_2_1 = "LEVEL_2_1"
    LEVEL_2_2 = "LEVEL_2_2"
    LEVEL_3 = "LEVEL_3"
    LEVEL_3_1 = "LEVEL_3_1"
    LEVEL_3_2 = "LEVEL_3_2"
    LEVEL_4 = "LEVEL_4"
    LEVEL_4_1 = "LEVEL_4_1"
    LEVEL_4_2 = "LEVEL_4_2"
    LEVEL_5 = "LEVEL_5"
    LEVEL_5_1 = "LEVEL_5_1"
    LEVEL_5_2 = "LEVEL_5_2"


class H264CodecProfile(StrEnum):
    BASELINE = "BASELINE"
    HIGH = "HIGH"
    HIGH_10BIT = "HIGH_10BIT"
    HIGH_422 = "HIGH_422"
    HIGH_422_10BIT = "HIGH_422_10BIT"
    MAIN = "MAIN"


class H264DynamicSubGop(StrEnum):
    ADAPTIVE = "ADAPTIVE"
    STATIC = "STATIC"


class H264EndOfStreamMarkers(StrEnum):
    INCLUDE = "INCLUDE"
    SUPPRESS = "SUPPRESS"


class H264EntropyEncoding(StrEnum):
    CABAC = "CABAC"
    CAVLC = "CAVLC"


class H264FieldEncoding(StrEnum):
    PAFF = "PAFF"
    FORCE_FIELD = "FORCE_FIELD"
    MBAFF = "MBAFF"


class H264FlickerAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264FramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264FramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class H264GopBReference(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264GopSizeUnits(StrEnum):
    FRAMES = "FRAMES"
    SECONDS = "SECONDS"
    AUTO = "AUTO"


class H264InterlaceMode(StrEnum):
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class H264ParControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264QualityTuningLevel(StrEnum):
    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class H264RateControlMode(StrEnum):
    VBR = "VBR"
    CBR = "CBR"
    QVBR = "QVBR"


class H264RepeatPps(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264SaliencyAwareEncoding(StrEnum):
    DISABLED = "DISABLED"
    PREFERRED = "PREFERRED"


class H264ScanTypeConversionMode(StrEnum):
    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class H264SceneChangeDetect(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    TRANSITION_DETECTION = "TRANSITION_DETECTION"


class H264SlowPal(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264SpatialAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264Syntax(StrEnum):
    DEFAULT = "DEFAULT"
    RP2027 = "RP2027"


class H264Telecine(StrEnum):
    NONE = "NONE"
    SOFT = "SOFT"
    HARD = "HARD"


class H264TemporalAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264UnregisteredSeiTimecode(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264WriteMp4PackagingType(StrEnum):
    AVC1 = "AVC1"
    AVC3 = "AVC3"


class H265AdaptiveQuantization(StrEnum):
    OFF = "OFF"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"
    AUTO = "AUTO"


class H265AlternateTransferFunctionSei(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265CodecLevel(StrEnum):
    AUTO = "AUTO"
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_2_1 = "LEVEL_2_1"
    LEVEL_3 = "LEVEL_3"
    LEVEL_3_1 = "LEVEL_3_1"
    LEVEL_4 = "LEVEL_4"
    LEVEL_4_1 = "LEVEL_4_1"
    LEVEL_5 = "LEVEL_5"
    LEVEL_5_1 = "LEVEL_5_1"
    LEVEL_5_2 = "LEVEL_5_2"
    LEVEL_6 = "LEVEL_6"
    LEVEL_6_1 = "LEVEL_6_1"
    LEVEL_6_2 = "LEVEL_6_2"


class H265CodecProfile(StrEnum):
    MAIN_MAIN = "MAIN_MAIN"
    MAIN_HIGH = "MAIN_HIGH"
    MAIN10_MAIN = "MAIN10_MAIN"
    MAIN10_HIGH = "MAIN10_HIGH"
    MAIN_422_8BIT_MAIN = "MAIN_422_8BIT_MAIN"
    MAIN_422_8BIT_HIGH = "MAIN_422_8BIT_HIGH"
    MAIN_422_10BIT_MAIN = "MAIN_422_10BIT_MAIN"
    MAIN_422_10BIT_HIGH = "MAIN_422_10BIT_HIGH"


class H265Deblocking(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class H265DynamicSubGop(StrEnum):
    ADAPTIVE = "ADAPTIVE"
    STATIC = "STATIC"


class H265EndOfStreamMarkers(StrEnum):
    INCLUDE = "INCLUDE"
    SUPPRESS = "SUPPRESS"


class H265FlickerAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265FramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H265FramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class H265GopBReference(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265GopSizeUnits(StrEnum):
    FRAMES = "FRAMES"
    SECONDS = "SECONDS"
    AUTO = "AUTO"


class H265InterlaceMode(StrEnum):
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class H265ParControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H265QualityTuningLevel(StrEnum):
    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class H265RateControlMode(StrEnum):
    VBR = "VBR"
    CBR = "CBR"
    QVBR = "QVBR"


class H265SampleAdaptiveOffsetFilterMode(StrEnum):
    DEFAULT = "DEFAULT"
    ADAPTIVE = "ADAPTIVE"
    OFF = "OFF"


class H265ScanTypeConversionMode(StrEnum):
    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class H265SceneChangeDetect(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    TRANSITION_DETECTION = "TRANSITION_DETECTION"


class H265SlowPal(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265SpatialAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265Telecine(StrEnum):
    NONE = "NONE"
    SOFT = "SOFT"
    HARD = "HARD"


class H265TemporalAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265TemporalIds(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265Tiles(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265UnregisteredSeiTimecode(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265WriteMp4PackagingType(StrEnum):
    HVC1 = "HVC1"
    HEV1 = "HEV1"


class HDRToSDRToneMapper(StrEnum):
    PRESERVE_DETAILS = "PRESERVE_DETAILS"
    VIBRANT = "VIBRANT"


class HlsAdMarkers(StrEnum):
    ELEMENTAL = "ELEMENTAL"
    ELEMENTAL_SCTE35 = "ELEMENTAL_SCTE35"


class HlsAudioOnlyContainer(StrEnum):
    AUTOMATIC = "AUTOMATIC"
    M2TS = "M2TS"


class HlsAudioOnlyHeader(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsAudioTrackType(StrEnum):
    ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT = "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT"
    ALTERNATE_AUDIO_AUTO_SELECT = "ALTERNATE_AUDIO_AUTO_SELECT"
    ALTERNATE_AUDIO_NOT_AUTO_SELECT = "ALTERNATE_AUDIO_NOT_AUTO_SELECT"
    AUDIO_ONLY_VARIANT_STREAM = "AUDIO_ONLY_VARIANT_STREAM"


class HlsCaptionLanguageSetting(StrEnum):
    INSERT = "INSERT"
    OMIT = "OMIT"
    NONE = "NONE"


class HlsCaptionSegmentLengthControl(StrEnum):
    LARGE_SEGMENTS = "LARGE_SEGMENTS"
    MATCH_VIDEO = "MATCH_VIDEO"


class HlsClientCache(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class HlsCodecSpecification(StrEnum):
    RFC_6381 = "RFC_6381"
    RFC_4281 = "RFC_4281"


class HlsDescriptiveVideoServiceFlag(StrEnum):
    DONT_FLAG = "DONT_FLAG"
    FLAG = "FLAG"


class HlsDirectoryStructure(StrEnum):
    SINGLE_DIRECTORY = "SINGLE_DIRECTORY"
    SUBDIRECTORY_PER_STREAM = "SUBDIRECTORY_PER_STREAM"


class HlsEncryptionType(StrEnum):
    AES128 = "AES128"
    SAMPLE_AES = "SAMPLE_AES"


class HlsIFrameOnlyManifest(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsImageBasedTrickPlay(StrEnum):
    NONE = "NONE"
    THUMBNAIL = "THUMBNAIL"
    THUMBNAIL_AND_FULLFRAME = "THUMBNAIL_AND_FULLFRAME"
    ADVANCED = "ADVANCED"


class HlsInitializationVectorInManifest(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsIntervalCadence(StrEnum):
    FOLLOW_IFRAME = "FOLLOW_IFRAME"
    FOLLOW_CUSTOM = "FOLLOW_CUSTOM"


class HlsKeyProviderType(StrEnum):
    SPEKE = "SPEKE"
    STATIC_KEY = "STATIC_KEY"


class HlsManifestCompression(StrEnum):
    GZIP = "GZIP"
    NONE = "NONE"


class HlsManifestDurationFormat(StrEnum):
    FLOATING_POINT = "FLOATING_POINT"
    INTEGER = "INTEGER"


class HlsOfflineEncrypted(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class HlsOutputSelection(StrEnum):
    MANIFESTS_AND_SEGMENTS = "MANIFESTS_AND_SEGMENTS"
    SEGMENTS_ONLY = "SEGMENTS_ONLY"


class HlsProgramDateTime(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsProgressiveWriteHlsManifest(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class HlsSegmentControl(StrEnum):
    SINGLE_FILE = "SINGLE_FILE"
    SEGMENTED_FILES = "SEGMENTED_FILES"


class HlsSegmentLengthControl(StrEnum):
    EXACT = "EXACT"
    GOP_MULTIPLE = "GOP_MULTIPLE"
    MATCH = "MATCH"


class HlsStreamInfResolution(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsTargetDurationCompatibilityMode(StrEnum):
    LEGACY = "LEGACY"
    SPEC_COMPLIANT = "SPEC_COMPLIANT"


class HlsTimedMetadataId3Frame(StrEnum):
    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


class ImscAccessibilitySubs(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class ImscStylePassthrough(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class InputDeblockFilter(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class InputDenoiseFilter(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class InputFilterEnable(StrEnum):
    AUTO = "AUTO"
    DISABLE = "DISABLE"
    FORCE = "FORCE"


class InputPolicy(StrEnum):
    ALLOWED = "ALLOWED"
    DISALLOWED = "DISALLOWED"


class InputPsiControl(StrEnum):
    IGNORE_PSI = "IGNORE_PSI"
    USE_PSI = "USE_PSI"


class InputRotate(StrEnum):
    DEGREE_0 = "DEGREE_0"
    DEGREES_90 = "DEGREES_90"
    DEGREES_180 = "DEGREES_180"
    DEGREES_270 = "DEGREES_270"
    AUTO = "AUTO"


class InputSampleRange(StrEnum):
    FOLLOW = "FOLLOW"
    FULL_RANGE = "FULL_RANGE"
    LIMITED_RANGE = "LIMITED_RANGE"


class InputScanType(StrEnum):
    AUTO = "AUTO"
    PSF = "PSF"


class InputTimecodeSource(StrEnum):
    EMBEDDED = "EMBEDDED"
    ZEROBASED = "ZEROBASED"
    SPECIFIEDSTART = "SPECIFIEDSTART"


class JobPhase(StrEnum):
    PROBING = "PROBING"
    TRANSCODING = "TRANSCODING"
    UPLOADING = "UPLOADING"


class JobStatus(StrEnum):
    SUBMITTED = "SUBMITTED"
    PROGRESSING = "PROGRESSING"
    COMPLETE = "COMPLETE"
    CANCELED = "CANCELED"
    ERROR = "ERROR"


class JobTemplateListBy(StrEnum):
    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"
    SYSTEM = "SYSTEM"


class LanguageCode(StrEnum):
    ENG = "ENG"
    SPA = "SPA"
    FRA = "FRA"
    DEU = "DEU"
    GER = "GER"
    ZHO = "ZHO"
    ARA = "ARA"
    HIN = "HIN"
    JPN = "JPN"
    RUS = "RUS"
    POR = "POR"
    ITA = "ITA"
    URD = "URD"
    VIE = "VIE"
    KOR = "KOR"
    PAN = "PAN"
    ABK = "ABK"
    AAR = "AAR"
    AFR = "AFR"
    AKA = "AKA"
    SQI = "SQI"
    AMH = "AMH"
    ARG = "ARG"
    HYE = "HYE"
    ASM = "ASM"
    AVA = "AVA"
    AVE = "AVE"
    AYM = "AYM"
    AZE = "AZE"
    BAM = "BAM"
    BAK = "BAK"
    EUS = "EUS"
    BEL = "BEL"
    BEN = "BEN"
    BIH = "BIH"
    BIS = "BIS"
    BOS = "BOS"
    BRE = "BRE"
    BUL = "BUL"
    MYA = "MYA"
    CAT = "CAT"
    KHM = "KHM"
    CHA = "CHA"
    CHE = "CHE"
    NYA = "NYA"
    CHU = "CHU"
    CHV = "CHV"
    COR = "COR"
    COS = "COS"
    CRE = "CRE"
    HRV = "HRV"
    CES = "CES"
    DAN = "DAN"
    DIV = "DIV"
    NLD = "NLD"
    DZO = "DZO"
    ENM = "ENM"
    EPO = "EPO"
    EST = "EST"
    EWE = "EWE"
    FAO = "FAO"
    FIJ = "FIJ"
    FIN = "FIN"
    FRM = "FRM"
    FUL = "FUL"
    GLA = "GLA"
    GLG = "GLG"
    LUG = "LUG"
    KAT = "KAT"
    ELL = "ELL"
    GRN = "GRN"
    GUJ = "GUJ"
    HAT = "HAT"
    HAU = "HAU"
    HEB = "HEB"
    HER = "HER"
    HMO = "HMO"
    HUN = "HUN"
    ISL = "ISL"
    IDO = "IDO"
    IBO = "IBO"
    IND = "IND"
    INA = "INA"
    ILE = "ILE"
    IKU = "IKU"
    IPK = "IPK"
    GLE = "GLE"
    JAV = "JAV"
    KAL = "KAL"
    KAN = "KAN"
    KAU = "KAU"
    KAS = "KAS"
    KAZ = "KAZ"
    KIK = "KIK"
    KIN = "KIN"
    KIR = "KIR"
    KOM = "KOM"
    KON = "KON"
    KUA = "KUA"
    KUR = "KUR"
    LAO = "LAO"
    LAT = "LAT"
    LAV = "LAV"
    LIM = "LIM"
    LIN = "LIN"
    LIT = "LIT"
    LUB = "LUB"
    LTZ = "LTZ"
    MKD = "MKD"
    MLG = "MLG"
    MSA = "MSA"
    MAL = "MAL"
    MLT = "MLT"
    GLV = "GLV"
    MRI = "MRI"
    MAR = "MAR"
    MAH = "MAH"
    MON = "MON"
    NAU = "NAU"
    NAV = "NAV"
    NDE = "NDE"
    NBL = "NBL"
    NDO = "NDO"
    NEP = "NEP"
    SME = "SME"
    NOR = "NOR"
    NOB = "NOB"
    NNO = "NNO"
    OCI = "OCI"
    OJI = "OJI"
    ORI = "ORI"
    ORM = "ORM"
    OSS = "OSS"
    PLI = "PLI"
    FAS = "FAS"
    POL = "POL"
    PUS = "PUS"
    QUE = "QUE"
    QAA = "QAA"
    RON = "RON"
    ROH = "ROH"
    RUN = "RUN"
    SMO = "SMO"
    SAG = "SAG"
    SAN = "SAN"
    SRD = "SRD"
    SRB = "SRB"
    SNA = "SNA"
    III = "III"
    SND = "SND"
    SIN = "SIN"
    SLK = "SLK"
    SLV = "SLV"
    SOM = "SOM"
    SOT = "SOT"
    SUN = "SUN"
    SWA = "SWA"
    SSW = "SSW"
    SWE = "SWE"
    TGL = "TGL"
    TAH = "TAH"
    TGK = "TGK"
    TAM = "TAM"
    TAT = "TAT"
    TEL = "TEL"
    THA = "THA"
    BOD = "BOD"
    TIR = "TIR"
    TON = "TON"
    TSO = "TSO"
    TSN = "TSN"
    TUR = "TUR"
    TUK = "TUK"
    TWI = "TWI"
    UIG = "UIG"
    UKR = "UKR"
    UZB = "UZB"
    VEN = "VEN"
    VOL = "VOL"
    WLN = "WLN"
    CYM = "CYM"
    FRY = "FRY"
    WOL = "WOL"
    XHO = "XHO"
    YID = "YID"
    YOR = "YOR"
    ZHA = "ZHA"
    ZUL = "ZUL"
    ORJ = "ORJ"
    QPC = "QPC"
    TNG = "TNG"
    SRP = "SRP"


class M2tsAudioBufferModel(StrEnum):
    DVB = "DVB"
    ATSC = "ATSC"


class M2tsAudioDuration(StrEnum):
    DEFAULT_CODEC_DURATION = "DEFAULT_CODEC_DURATION"
    MATCH_VIDEO_DURATION = "MATCH_VIDEO_DURATION"


class M2tsBufferModel(StrEnum):
    MULTIPLEX = "MULTIPLEX"
    NONE = "NONE"


class M2tsDataPtsControl(StrEnum):
    AUTO = "AUTO"
    ALIGN_TO_VIDEO = "ALIGN_TO_VIDEO"


class M2tsEbpAudioInterval(StrEnum):
    VIDEO_AND_FIXED_INTERVALS = "VIDEO_AND_FIXED_INTERVALS"
    VIDEO_INTERVAL = "VIDEO_INTERVAL"


class M2tsEbpPlacement(StrEnum):
    VIDEO_AND_AUDIO_PIDS = "VIDEO_AND_AUDIO_PIDS"
    VIDEO_PID = "VIDEO_PID"


class M2tsEsRateInPes(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class M2tsForceTsVideoEbpOrder(StrEnum):
    FORCE = "FORCE"
    DEFAULT = "DEFAULT"


class M2tsKlvMetadata(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class M2tsNielsenId3(StrEnum):
    INSERT = "INSERT"
    NONE = "NONE"


class M2tsPcrControl(StrEnum):
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"


class M2tsPreventBufferUnderflow(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class M2tsRateMode(StrEnum):
    VBR = "VBR"
    CBR = "CBR"


class M2tsScte35Source(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class M2tsSegmentationMarkers(StrEnum):
    NONE = "NONE"
    RAI_SEGSTART = "RAI_SEGSTART"
    RAI_ADAPT = "RAI_ADAPT"
    PSI_SEGSTART = "PSI_SEGSTART"
    EBP = "EBP"
    EBP_LEGACY = "EBP_LEGACY"


class M2tsSegmentationStyle(StrEnum):
    MAINTAIN_CADENCE = "MAINTAIN_CADENCE"
    RESET_CADENCE = "RESET_CADENCE"


class M3u8AudioDuration(StrEnum):
    DEFAULT_CODEC_DURATION = "DEFAULT_CODEC_DURATION"
    MATCH_VIDEO_DURATION = "MATCH_VIDEO_DURATION"


class M3u8DataPtsControl(StrEnum):
    AUTO = "AUTO"
    ALIGN_TO_VIDEO = "ALIGN_TO_VIDEO"


class M3u8NielsenId3(StrEnum):
    INSERT = "INSERT"
    NONE = "NONE"


class M3u8PcrControl(StrEnum):
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"


class M3u8Scte35Source(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class MatrixCoefficients(StrEnum):
    RGB = "RGB"
    ITU_709 = "ITU_709"
    UNSPECIFIED = "UNSPECIFIED"
    RESERVED = "RESERVED"
    FCC = "FCC"
    ITU_470BG = "ITU_470BG"
    SMPTE_170M = "SMPTE_170M"
    SMPTE_240M = "SMPTE_240M"
    YCgCo = "YCgCo"
    ITU_2020_NCL = "ITU_2020_NCL"
    ITU_2020_CL = "ITU_2020_CL"
    SMPTE_2085 = "SMPTE_2085"
    CD_NCL = "CD_NCL"
    CD_CL = "CD_CL"
    ITU_2100ICtCp = "ITU_2100ICtCp"
    IPT = "IPT"
    EBU3213 = "EBU3213"
    LAST = "LAST"


class MotionImageInsertionMode(StrEnum):
    MOV = "MOV"
    PNG = "PNG"


class MotionImagePlayback(StrEnum):
    ONCE = "ONCE"
    REPEAT = "REPEAT"


class MovClapAtom(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class MovCslgAtom(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class MovMpeg2FourCCControl(StrEnum):
    XDCAM = "XDCAM"
    MPEG = "MPEG"


class MovPaddingControl(StrEnum):
    OMNEON = "OMNEON"
    NONE = "NONE"


class MovReference(StrEnum):
    SELF_CONTAINED = "SELF_CONTAINED"
    EXTERNAL = "EXTERNAL"


class Mp3RateControlMode(StrEnum):
    CBR = "CBR"
    VBR = "VBR"


class Mp4CslgAtom(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class Mp4FreeSpaceBox(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class Mp4MoovPlacement(StrEnum):
    PROGRESSIVE_DOWNLOAD = "PROGRESSIVE_DOWNLOAD"
    NORMAL = "NORMAL"


class MpdAccessibilityCaptionHints(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class MpdAudioDuration(StrEnum):
    DEFAULT_CODEC_DURATION = "DEFAULT_CODEC_DURATION"
    MATCH_VIDEO_DURATION = "MATCH_VIDEO_DURATION"


class MpdCaptionContainerType(StrEnum):
    RAW = "RAW"
    FRAGMENTED_MP4 = "FRAGMENTED_MP4"


class MpdKlvMetadata(StrEnum):
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class MpdManifestMetadataSignaling(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MpdScte35Esam(StrEnum):
    INSERT = "INSERT"
    NONE = "NONE"


class MpdScte35Source(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class MpdTimedMetadata(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class MpdTimedMetadataBoxVersion(StrEnum):
    VERSION_0 = "VERSION_0"
    VERSION_1 = "VERSION_1"


class Mpeg2AdaptiveQuantization(StrEnum):
    OFF = "OFF"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Mpeg2CodecLevel(StrEnum):
    AUTO = "AUTO"
    LOW = "LOW"
    MAIN = "MAIN"
    HIGH1440 = "HIGH1440"
    HIGH = "HIGH"


class Mpeg2CodecProfile(StrEnum):
    MAIN = "MAIN"
    PROFILE_422 = "PROFILE_422"


class Mpeg2DynamicSubGop(StrEnum):
    ADAPTIVE = "ADAPTIVE"
    STATIC = "STATIC"


class Mpeg2FramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Mpeg2FramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Mpeg2GopSizeUnits(StrEnum):
    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class Mpeg2InterlaceMode(StrEnum):
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class Mpeg2IntraDcPrecision(StrEnum):
    AUTO = "AUTO"
    INTRA_DC_PRECISION_8 = "INTRA_DC_PRECISION_8"
    INTRA_DC_PRECISION_9 = "INTRA_DC_PRECISION_9"
    INTRA_DC_PRECISION_10 = "INTRA_DC_PRECISION_10"
    INTRA_DC_PRECISION_11 = "INTRA_DC_PRECISION_11"


class Mpeg2ParControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Mpeg2QualityTuningLevel(StrEnum):
    SINGLE_PASS = "SINGLE_PASS"
    MULTI_PASS = "MULTI_PASS"


class Mpeg2RateControlMode(StrEnum):
    VBR = "VBR"
    CBR = "CBR"


class Mpeg2ScanTypeConversionMode(StrEnum):
    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class Mpeg2SceneChangeDetect(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Mpeg2SlowPal(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Mpeg2SpatialAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Mpeg2Syntax(StrEnum):
    DEFAULT = "DEFAULT"
    D_10 = "D_10"


class Mpeg2Telecine(StrEnum):
    NONE = "NONE"
    SOFT = "SOFT"
    HARD = "HARD"


class Mpeg2TemporalAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class MsSmoothAudioDeduplication(StrEnum):
    COMBINE_DUPLICATE_STREAMS = "COMBINE_DUPLICATE_STREAMS"
    NONE = "NONE"


class MsSmoothFragmentLengthControl(StrEnum):
    EXACT = "EXACT"
    GOP_MULTIPLE = "GOP_MULTIPLE"


class MsSmoothManifestEncoding(StrEnum):
    UTF8 = "UTF8"
    UTF16 = "UTF16"


class MxfAfdSignaling(StrEnum):
    NO_COPY = "NO_COPY"
    COPY_FROM_VIDEO = "COPY_FROM_VIDEO"


class MxfProfile(StrEnum):
    D_10 = "D_10"
    XDCAM = "XDCAM"
    OP1A = "OP1A"
    XAVC = "XAVC"
    XDCAM_RDD9 = "XDCAM_RDD9"


class MxfXavcDurationMode(StrEnum):
    ALLOW_ANY_DURATION = "ALLOW_ANY_DURATION"
    DROP_FRAMES_FOR_COMPLIANCE = "DROP_FRAMES_FOR_COMPLIANCE"


class NielsenActiveWatermarkProcessType(StrEnum):
    NAES2_AND_NW = "NAES2_AND_NW"
    CBET = "CBET"
    NAES2_AND_NW_AND_CBET = "NAES2_AND_NW_AND_CBET"


class NielsenSourceWatermarkStatusType(StrEnum):
    CLEAN = "CLEAN"
    WATERMARKED = "WATERMARKED"


class NielsenUniqueTicPerAudioTrackType(StrEnum):
    RESERVE_UNIQUE_TICS_PER_TRACK = "RESERVE_UNIQUE_TICS_PER_TRACK"
    SAME_TICS_PER_TRACK = "SAME_TICS_PER_TRACK"


class NoiseFilterPostTemporalSharpening(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    AUTO = "AUTO"


class NoiseFilterPostTemporalSharpeningStrength(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class NoiseReducerFilter(StrEnum):
    BILATERAL = "BILATERAL"
    MEAN = "MEAN"
    GAUSSIAN = "GAUSSIAN"
    LANCZOS = "LANCZOS"
    SHARPEN = "SHARPEN"
    CONSERVE = "CONSERVE"
    SPATIAL = "SPATIAL"
    TEMPORAL = "TEMPORAL"


class Order(StrEnum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class OutputGroupType(StrEnum):
    HLS_GROUP_SETTINGS = "HLS_GROUP_SETTINGS"
    DASH_ISO_GROUP_SETTINGS = "DASH_ISO_GROUP_SETTINGS"
    FILE_GROUP_SETTINGS = "FILE_GROUP_SETTINGS"
    MS_SMOOTH_GROUP_SETTINGS = "MS_SMOOTH_GROUP_SETTINGS"
    CMAF_GROUP_SETTINGS = "CMAF_GROUP_SETTINGS"


class OutputSdt(StrEnum):
    SDT_FOLLOW = "SDT_FOLLOW"
    SDT_FOLLOW_IF_PRESENT = "SDT_FOLLOW_IF_PRESENT"
    SDT_MANUAL = "SDT_MANUAL"
    SDT_NONE = "SDT_NONE"


class PadVideo(StrEnum):
    DISABLED = "DISABLED"
    BLACK = "BLACK"


class PresetListBy(StrEnum):
    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"
    SYSTEM = "SYSTEM"


class PresetSpeke20Audio(StrEnum):
    PRESET_AUDIO_1 = "PRESET_AUDIO_1"
    PRESET_AUDIO_2 = "PRESET_AUDIO_2"
    PRESET_AUDIO_3 = "PRESET_AUDIO_3"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class PresetSpeke20Video(StrEnum):
    PRESET_VIDEO_1 = "PRESET_VIDEO_1"
    PRESET_VIDEO_2 = "PRESET_VIDEO_2"
    PRESET_VIDEO_3 = "PRESET_VIDEO_3"
    PRESET_VIDEO_4 = "PRESET_VIDEO_4"
    PRESET_VIDEO_5 = "PRESET_VIDEO_5"
    PRESET_VIDEO_6 = "PRESET_VIDEO_6"
    PRESET_VIDEO_7 = "PRESET_VIDEO_7"
    PRESET_VIDEO_8 = "PRESET_VIDEO_8"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class PricingPlan(StrEnum):
    ON_DEMAND = "ON_DEMAND"
    RESERVED = "RESERVED"


class ProresChromaSampling(StrEnum):
    PRESERVE_444_SAMPLING = "PRESERVE_444_SAMPLING"
    SUBSAMPLE_TO_422 = "SUBSAMPLE_TO_422"


class ProresCodecProfile(StrEnum):
    APPLE_PRORES_422 = "APPLE_PRORES_422"
    APPLE_PRORES_422_HQ = "APPLE_PRORES_422_HQ"
    APPLE_PRORES_422_LT = "APPLE_PRORES_422_LT"
    APPLE_PRORES_422_PROXY = "APPLE_PRORES_422_PROXY"
    APPLE_PRORES_4444 = "APPLE_PRORES_4444"
    APPLE_PRORES_4444_XQ = "APPLE_PRORES_4444_XQ"


class ProresFramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class ProresFramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class ProresInterlaceMode(StrEnum):
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class ProresParControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class ProresScanTypeConversionMode(StrEnum):
    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class ProresSlowPal(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class ProresTelecine(StrEnum):
    NONE = "NONE"
    HARD = "HARD"


class QueueListBy(StrEnum):
    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"


class QueueStatus(StrEnum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class RemoveRubyReserveAttributes(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class RenewalType(StrEnum):
    AUTO_RENEW = "AUTO_RENEW"
    EXPIRE = "EXPIRE"


class RequiredFlag(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ReservationPlanStatus(StrEnum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"


class RespondToAfd(StrEnum):
    NONE = "NONE"
    RESPOND = "RESPOND"
    PASSTHROUGH = "PASSTHROUGH"


class RuleType(StrEnum):
    MIN_TOP_RENDITION_SIZE = "MIN_TOP_RENDITION_SIZE"
    MIN_BOTTOM_RENDITION_SIZE = "MIN_BOTTOM_RENDITION_SIZE"
    FORCE_INCLUDE_RENDITIONS = "FORCE_INCLUDE_RENDITIONS"
    ALLOWED_RENDITIONS = "ALLOWED_RENDITIONS"


class S3ObjectCannedAcl(StrEnum):
    PUBLIC_READ = "PUBLIC_READ"
    AUTHENTICATED_READ = "AUTHENTICATED_READ"
    BUCKET_OWNER_READ = "BUCKET_OWNER_READ"
    BUCKET_OWNER_FULL_CONTROL = "BUCKET_OWNER_FULL_CONTROL"


class S3ServerSideEncryptionType(StrEnum):
    SERVER_SIDE_ENCRYPTION_S3 = "SERVER_SIDE_ENCRYPTION_S3"
    SERVER_SIDE_ENCRYPTION_KMS = "SERVER_SIDE_ENCRYPTION_KMS"


class S3StorageClass(StrEnum):
    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    GLACIER = "GLACIER"
    DEEP_ARCHIVE = "DEEP_ARCHIVE"


class SampleRangeConversion(StrEnum):
    LIMITED_RANGE_SQUEEZE = "LIMITED_RANGE_SQUEEZE"
    NONE = "NONE"
    LIMITED_RANGE_CLIP = "LIMITED_RANGE_CLIP"


class ScalingBehavior(StrEnum):
    DEFAULT = "DEFAULT"
    STRETCH_TO_OUTPUT = "STRETCH_TO_OUTPUT"
    FIT = "FIT"
    FIT_NO_UPSCALE = "FIT_NO_UPSCALE"
    FILL = "FILL"


class SccDestinationFramerate(StrEnum):
    FRAMERATE_23_97 = "FRAMERATE_23_97"
    FRAMERATE_24 = "FRAMERATE_24"
    FRAMERATE_25 = "FRAMERATE_25"
    FRAMERATE_29_97_DROPFRAME = "FRAMERATE_29_97_DROPFRAME"
    FRAMERATE_29_97_NON_DROPFRAME = "FRAMERATE_29_97_NON_DROPFRAME"


class SimulateReservedQueue(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class SrtStylePassthrough(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class StatusUpdateInterval(StrEnum):
    SECONDS_10 = "SECONDS_10"
    SECONDS_12 = "SECONDS_12"
    SECONDS_15 = "SECONDS_15"
    SECONDS_20 = "SECONDS_20"
    SECONDS_30 = "SECONDS_30"
    SECONDS_60 = "SECONDS_60"
    SECONDS_120 = "SECONDS_120"
    SECONDS_180 = "SECONDS_180"
    SECONDS_240 = "SECONDS_240"
    SECONDS_300 = "SECONDS_300"
    SECONDS_360 = "SECONDS_360"
    SECONDS_420 = "SECONDS_420"
    SECONDS_480 = "SECONDS_480"
    SECONDS_540 = "SECONDS_540"
    SECONDS_600 = "SECONDS_600"


class TeletextPageType(StrEnum):
    PAGE_TYPE_INITIAL = "PAGE_TYPE_INITIAL"
    PAGE_TYPE_SUBTITLE = "PAGE_TYPE_SUBTITLE"
    PAGE_TYPE_ADDL_INFO = "PAGE_TYPE_ADDL_INFO"
    PAGE_TYPE_PROGRAM_SCHEDULE = "PAGE_TYPE_PROGRAM_SCHEDULE"
    PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE = "PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE"


class TimecodeBurninPosition(StrEnum):
    TOP_CENTER = "TOP_CENTER"
    TOP_LEFT = "TOP_LEFT"
    TOP_RIGHT = "TOP_RIGHT"
    MIDDLE_LEFT = "MIDDLE_LEFT"
    MIDDLE_CENTER = "MIDDLE_CENTER"
    MIDDLE_RIGHT = "MIDDLE_RIGHT"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BOTTOM_CENTER = "BOTTOM_CENTER"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"


class TimecodeSource(StrEnum):
    EMBEDDED = "EMBEDDED"
    ZEROBASED = "ZEROBASED"
    SPECIFIEDSTART = "SPECIFIEDSTART"


class TimecodeTrack(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class TimedMetadata(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class TrackType(StrEnum):
    video = "video"
    audio = "audio"
    data = "data"


class TransferCharacteristics(StrEnum):
    ITU_709 = "ITU_709"
    UNSPECIFIED = "UNSPECIFIED"
    RESERVED = "RESERVED"
    ITU_470M = "ITU_470M"
    ITU_470BG = "ITU_470BG"
    SMPTE_170M = "SMPTE_170M"
    SMPTE_240M = "SMPTE_240M"
    LINEAR = "LINEAR"
    LOG10_2 = "LOG10_2"
    LOC10_2_5 = "LOC10_2_5"
    IEC_61966_2_4 = "IEC_61966_2_4"
    ITU_1361 = "ITU_1361"
    IEC_61966_2_1 = "IEC_61966_2_1"
    ITU_2020_10bit = "ITU_2020_10bit"
    ITU_2020_12bit = "ITU_2020_12bit"
    SMPTE_2084 = "SMPTE_2084"
    SMPTE_428_1 = "SMPTE_428_1"
    ARIB_B67 = "ARIB_B67"
    LAST = "LAST"


class TsPtsOffset(StrEnum):
    AUTO = "AUTO"
    SECONDS = "SECONDS"
    MILLISECONDS = "MILLISECONDS"


class TtmlStylePassthrough(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Type(StrEnum):
    SYSTEM = "SYSTEM"
    CUSTOM = "CUSTOM"


class UncompressedFourcc(StrEnum):
    I420 = "I420"
    I422 = "I422"
    I444 = "I444"


class UncompressedFramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class UncompressedFramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class UncompressedInterlaceMode(StrEnum):
    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class UncompressedScanTypeConversionMode(StrEnum):
    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class UncompressedSlowPal(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class UncompressedTelecine(StrEnum):
    NONE = "NONE"
    HARD = "HARD"


class Vc3Class(StrEnum):
    CLASS_145_8BIT = "CLASS_145_8BIT"
    CLASS_220_8BIT = "CLASS_220_8BIT"
    CLASS_220_10BIT = "CLASS_220_10BIT"


class Vc3FramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vc3FramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Vc3InterlaceMode(StrEnum):
    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class Vc3ScanTypeConversionMode(StrEnum):
    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class Vc3SlowPal(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Vc3Telecine(StrEnum):
    NONE = "NONE"
    HARD = "HARD"


class VchipAction(StrEnum):
    PASSTHROUGH = "PASSTHROUGH"
    STRIP = "STRIP"


class VideoCodec(StrEnum):
    AV1 = "AV1"
    AVC_INTRA = "AVC_INTRA"
    FRAME_CAPTURE = "FRAME_CAPTURE"
    GIF = "GIF"
    H_264 = "H_264"
    H_265 = "H_265"
    MPEG2 = "MPEG2"
    PASSTHROUGH = "PASSTHROUGH"
    PRORES = "PRORES"
    UNCOMPRESSED = "UNCOMPRESSED"
    VC3 = "VC3"
    VP8 = "VP8"
    VP9 = "VP9"
    XAVC = "XAVC"


class VideoOverlayPlayBackMode(StrEnum):
    ONCE = "ONCE"
    REPEAT = "REPEAT"


class VideoOverlayUnit(StrEnum):
    PIXELS = "PIXELS"
    PERCENTAGE = "PERCENTAGE"


class VideoTimecodeInsertion(StrEnum):
    DISABLED = "DISABLED"
    PIC_TIMING_SEI = "PIC_TIMING_SEI"


class Vp8FramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vp8FramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Vp8ParControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vp8QualityTuningLevel(StrEnum):
    MULTI_PASS = "MULTI_PASS"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class Vp8RateControlMode(StrEnum):
    VBR = "VBR"


class Vp9FramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vp9FramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Vp9ParControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vp9QualityTuningLevel(StrEnum):
    MULTI_PASS = "MULTI_PASS"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class Vp9RateControlMode(StrEnum):
    VBR = "VBR"


class WatermarkingStrength(StrEnum):
    LIGHTEST = "LIGHTEST"
    LIGHTER = "LIGHTER"
    DEFAULT = "DEFAULT"
    STRONGER = "STRONGER"
    STRONGEST = "STRONGEST"


class WavFormat(StrEnum):
    RIFF = "RIFF"
    RF64 = "RF64"
    EXTENSIBLE = "EXTENSIBLE"


class WebvttAccessibilitySubs(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class WebvttStylePassthrough(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    STRICT = "STRICT"
    MERGE = "MERGE"


class Xavc4kIntraCbgProfileClass(StrEnum):
    CLASS_100 = "CLASS_100"
    CLASS_300 = "CLASS_300"
    CLASS_480 = "CLASS_480"


class Xavc4kIntraVbrProfileClass(StrEnum):
    CLASS_100 = "CLASS_100"
    CLASS_300 = "CLASS_300"
    CLASS_480 = "CLASS_480"


class Xavc4kProfileBitrateClass(StrEnum):
    BITRATE_CLASS_100 = "BITRATE_CLASS_100"
    BITRATE_CLASS_140 = "BITRATE_CLASS_140"
    BITRATE_CLASS_200 = "BITRATE_CLASS_200"


class Xavc4kProfileCodecProfile(StrEnum):
    HIGH = "HIGH"
    HIGH_422 = "HIGH_422"


class Xavc4kProfileQualityTuningLevel(StrEnum):
    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class XavcAdaptiveQuantization(StrEnum):
    OFF = "OFF"
    AUTO = "AUTO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"


class XavcEntropyEncoding(StrEnum):
    AUTO = "AUTO"
    CABAC = "CABAC"
    CAVLC = "CAVLC"


class XavcFlickerAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class XavcFramerateControl(StrEnum):
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class XavcFramerateConversionAlgorithm(StrEnum):
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class XavcGopBReference(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class XavcHdIntraCbgProfileClass(StrEnum):
    CLASS_50 = "CLASS_50"
    CLASS_100 = "CLASS_100"
    CLASS_200 = "CLASS_200"


class XavcHdProfileBitrateClass(StrEnum):
    BITRATE_CLASS_25 = "BITRATE_CLASS_25"
    BITRATE_CLASS_35 = "BITRATE_CLASS_35"
    BITRATE_CLASS_50 = "BITRATE_CLASS_50"


class XavcHdProfileQualityTuningLevel(StrEnum):
    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class XavcHdProfileTelecine(StrEnum):
    NONE = "NONE"
    HARD = "HARD"


class XavcInterlaceMode(StrEnum):
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class XavcProfile(StrEnum):
    XAVC_HD_INTRA_CBG = "XAVC_HD_INTRA_CBG"
    XAVC_4K_INTRA_CBG = "XAVC_4K_INTRA_CBG"
    XAVC_4K_INTRA_VBR = "XAVC_4K_INTRA_VBR"
    XAVC_HD = "XAVC_HD"
    XAVC_4K = "XAVC_4K"


class XavcSlowPal(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class XavcSpatialAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class XavcTemporalAdaptiveQuantization(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class BadRequestException(ServiceException):
    """The service can't process your request because of a problem in the
    request. Please check your request form and syntax.
    """

    code: str = "BadRequestException"
    sender_fault: bool = False
    status_code: int = 400


class ConflictException(ServiceException):
    """The service couldn't complete your request because there is a conflict
    with the current state of the resource.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 409


class ForbiddenException(ServiceException):
    """You don't have permissions for this action with the credentials you
    sent.
    """

    code: str = "ForbiddenException"
    sender_fault: bool = False
    status_code: int = 403


class InternalServerErrorException(ServiceException):
    """The service encountered an unexpected condition and can't fulfill your
    request.
    """

    code: str = "InternalServerErrorException"
    sender_fault: bool = False
    status_code: int = 500


class NotFoundException(ServiceException):
    """The resource you requested doesn't exist."""

    code: str = "NotFoundException"
    sender_fault: bool = False
    status_code: int = 404


class TooManyRequestsException(ServiceException):
    """Too many requests have been sent in too short of a time. The service
    limits the rate at which it will accept requests.
    """

    code: str = "TooManyRequestsException"
    sender_fault: bool = False
    status_code: int = 429


class AacSettings(TypedDict, total=False):
    """Required when you set Codec to the value AAC. The service accepts one of
    two mutually exclusive groups of AAC settings--VBR and CBR. To select
    one of these modes, set the value of Bitrate control mode to "VBR" or
    "CBR". In VBR mode, you control the audio quality with the setting VBR
    quality. In CBR mode, you use the setting Bitrate. Defaults and valid
    values depend on the rate control mode.
    """

    AudioDescriptionBroadcasterMix: Optional[AacAudioDescriptionBroadcasterMix]
    Bitrate: Optional[_integerMin6000Max1024000]
    CodecProfile: Optional[AacCodecProfile]
    CodingMode: Optional[AacCodingMode]
    RateControlMode: Optional[AacRateControlMode]
    RawFormat: Optional[AacRawFormat]
    SampleRate: Optional[_integerMin8000Max96000]
    Specification: Optional[AacSpecification]
    VbrQuality: Optional[AacVbrQuality]


class Ac3Settings(TypedDict, total=False):
    """Required when you set Codec to the value AC3."""

    Bitrate: Optional[_integerMin64000Max640000]
    BitstreamMode: Optional[Ac3BitstreamMode]
    CodingMode: Optional[Ac3CodingMode]
    Dialnorm: Optional[_integerMin1Max31]
    DynamicRangeCompressionLine: Optional[Ac3DynamicRangeCompressionLine]
    DynamicRangeCompressionProfile: Optional[Ac3DynamicRangeCompressionProfile]
    DynamicRangeCompressionRf: Optional[Ac3DynamicRangeCompressionRf]
    LfeFilter: Optional[Ac3LfeFilter]
    MetadataControl: Optional[Ac3MetadataControl]
    SampleRate: Optional[_integerMin48000Max48000]


class AccelerationSettings(TypedDict, total=False):
    """Accelerated transcoding can significantly speed up jobs with long,
    visually complex content.
    """

    Mode: AccelerationMode


class AdvancedInputFilterSettings(TypedDict, total=False):
    """Optional settings for Advanced input filter when you set Advanced input
    filter to Enabled.
    """

    AddTexture: Optional[AdvancedInputFilterAddTexture]
    Sharpening: Optional[AdvancedInputFilterSharpen]


class AiffSettings(TypedDict, total=False):
    """Required when you set Codec to the value AIFF."""

    BitDepth: Optional[_integerMin16Max24]
    Channels: Optional[_integerMin1Max64]
    SampleRate: Optional[_integerMin8000Max192000]


class AllowedRenditionSize(TypedDict, total=False):
    """Use Allowed renditions to specify a list of possible resolutions in your
    ABR stack. \\* MediaConvert will create an ABR stack exclusively from the
    list of resolutions that you specify. \\* Some resolutions in the Allowed
    renditions list may not be included, however you can force a resolution
    to be included by setting Required to ENABLED. \\* You must specify at
    least one resolution that is greater than or equal to any resolutions
    that you specify in Min top rendition size or Min bottom rendition size.
    \\* If you specify Allowed renditions, you must not specify a separate
    rule for Force include renditions.
    """

    Height: Optional[_integerMin32Max8192]
    Required: Optional[RequiredFlag]
    Width: Optional[_integerMin32Max8192]


class AncillarySourceSettings(TypedDict, total=False):
    """Settings for ancillary captions source."""

    Convert608To708: Optional[AncillaryConvert608To708]
    SourceAncillaryChannelNumber: Optional[_integerMin1Max4]
    TerminateCaptions: Optional[AncillaryTerminateCaptions]


class AssociateCertificateRequest(ServiceRequest):
    Arn: _string


class AssociateCertificateResponse(TypedDict, total=False):
    pass


_listOfAudioChannelTag = List[AudioChannelTag]


class AudioChannelTaggingSettings(TypedDict, total=False):
    """Specify the QuickTime audio channel layout tags for the audio channels
    in this audio track. When you don't specify a value, MediaConvert labels
    your track as Center (C) by default. To use Audio layout tagging, your
    output must be in a QuickTime (MOV) container and your audio codec must
    be AAC, WAV, or AIFF.
    """

    ChannelTag: Optional[AudioChannelTag]
    ChannelTags: Optional[_listOfAudioChannelTag]


class WavSettings(TypedDict, total=False):
    """Required when you set Codec to the value WAV."""

    BitDepth: Optional[_integerMin16Max24]
    Channels: Optional[_integerMin1Max64]
    Format: Optional[WavFormat]
    SampleRate: Optional[_integerMin8000Max192000]


class VorbisSettings(TypedDict, total=False):
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to
    the value Vorbis.
    """

    Channels: Optional[_integerMin1Max2]
    SampleRate: Optional[_integerMin22050Max48000]
    VbrQuality: Optional[_integerMinNegative1Max10]


class OpusSettings(TypedDict, total=False):
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to
    the value OPUS.
    """

    Bitrate: Optional[_integerMin32000Max192000]
    Channels: Optional[_integerMin1Max2]
    SampleRate: Optional[_integerMin16000Max48000]


class Mp3Settings(TypedDict, total=False):
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to
    the value MP3.
    """

    Bitrate: Optional[_integerMin16000Max320000]
    Channels: Optional[_integerMin1Max2]
    RateControlMode: Optional[Mp3RateControlMode]
    SampleRate: Optional[_integerMin22050Max48000]
    VbrQuality: Optional[_integerMin0Max9]


class Mp2Settings(TypedDict, total=False):
    """Required when you set Codec to the value MP2."""

    Bitrate: Optional[_integerMin32000Max384000]
    Channels: Optional[_integerMin1Max2]
    SampleRate: Optional[_integerMin32000Max48000]


class FlacSettings(TypedDict, total=False):
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to
    the value FLAC.
    """

    BitDepth: Optional[_integerMin16Max24]
    Channels: Optional[_integerMin1Max8]
    SampleRate: Optional[_integerMin22050Max48000]


class Eac3Settings(TypedDict, total=False):
    """Required when you set Codec to the value EAC3."""

    AttenuationControl: Optional[Eac3AttenuationControl]
    Bitrate: Optional[_integerMin32000Max3024000]
    BitstreamMode: Optional[Eac3BitstreamMode]
    CodingMode: Optional[Eac3CodingMode]
    DcFilter: Optional[Eac3DcFilter]
    Dialnorm: Optional[_integerMin1Max31]
    DynamicRangeCompressionLine: Optional[Eac3DynamicRangeCompressionLine]
    DynamicRangeCompressionRf: Optional[Eac3DynamicRangeCompressionRf]
    LfeControl: Optional[Eac3LfeControl]
    LfeFilter: Optional[Eac3LfeFilter]
    LoRoCenterMixLevel: Optional[_doubleMinNegative60Max3]
    LoRoSurroundMixLevel: Optional[_doubleMinNegative60MaxNegative1]
    LtRtCenterMixLevel: Optional[_doubleMinNegative60Max3]
    LtRtSurroundMixLevel: Optional[_doubleMinNegative60MaxNegative1]
    MetadataControl: Optional[Eac3MetadataControl]
    PassthroughControl: Optional[Eac3PassthroughControl]
    PhaseControl: Optional[Eac3PhaseControl]
    SampleRate: Optional[_integerMin48000Max48000]
    StereoDownmix: Optional[Eac3StereoDownmix]
    SurroundExMode: Optional[Eac3SurroundExMode]
    SurroundMode: Optional[Eac3SurroundMode]


class Eac3AtmosSettings(TypedDict, total=False):
    """Required when you set Codec to the value EAC3_ATMOS."""

    Bitrate: Optional[_integerMin384000Max1024000]
    BitstreamMode: Optional[Eac3AtmosBitstreamMode]
    CodingMode: Optional[Eac3AtmosCodingMode]
    DialogueIntelligence: Optional[Eac3AtmosDialogueIntelligence]
    DownmixControl: Optional[Eac3AtmosDownmixControl]
    DynamicRangeCompressionLine: Optional[Eac3AtmosDynamicRangeCompressionLine]
    DynamicRangeCompressionRf: Optional[Eac3AtmosDynamicRangeCompressionRf]
    DynamicRangeControl: Optional[Eac3AtmosDynamicRangeControl]
    LoRoCenterMixLevel: Optional[_doubleMinNegative6Max3]
    LoRoSurroundMixLevel: Optional[_doubleMinNegative60MaxNegative1]
    LtRtCenterMixLevel: Optional[_doubleMinNegative6Max3]
    LtRtSurroundMixLevel: Optional[_doubleMinNegative60MaxNegative1]
    MeteringMode: Optional[Eac3AtmosMeteringMode]
    SampleRate: Optional[_integerMin48000Max48000]
    SpeechThreshold: Optional[_integerMin0Max100]
    StereoDownmix: Optional[Eac3AtmosStereoDownmix]
    SurroundExMode: Optional[Eac3AtmosSurroundExMode]


class AudioCodecSettings(TypedDict, total=False):
    """Settings related to audio encoding. The settings in this group vary
    depending on the value that you choose for your audio codec.
    """

    AacSettings: Optional[AacSettings]
    Ac3Settings: Optional[Ac3Settings]
    AiffSettings: Optional[AiffSettings]
    Codec: Optional[AudioCodec]
    Eac3AtmosSettings: Optional[Eac3AtmosSettings]
    Eac3Settings: Optional[Eac3Settings]
    FlacSettings: Optional[FlacSettings]
    Mp2Settings: Optional[Mp2Settings]
    Mp3Settings: Optional[Mp3Settings]
    OpusSettings: Optional[OpusSettings]
    VorbisSettings: Optional[VorbisSettings]
    WavSettings: Optional[WavSettings]


_listOf__doubleMinNegative60Max6 = List[_doubleMinNegative60Max6]
_listOf__integerMinNegative60Max6 = List[_integerMinNegative60Max6]


class OutputChannelMapping(TypedDict, total=False):
    """OutputChannel mapping settings."""

    InputChannels: Optional[_listOf__integerMinNegative60Max6]
    InputChannelsFineTune: Optional[_listOf__doubleMinNegative60Max6]


_listOfOutputChannelMapping = List[OutputChannelMapping]


class ChannelMapping(TypedDict, total=False):
    """Channel mapping contains the group of fields that hold the remixing
    value for each channel, in dB. Specify remix values to indicate how much
    of the content from your input audio channel you want in your output
    audio channels. Each instance of the InputChannels or
    InputChannelsFineTune array specifies these values for one output
    channel. Use one instance of this array for each output channel. In the
    console, each array corresponds to a column in the graphical depiction
    of the mapping matrix. The rows of the graphical matrix correspond to
    input channels. Valid values are within the range from -60 (mute)
    through 6. A setting of 0 passes the input channel unchanged to the
    output channel (no attenuation or amplification). Use InputChannels or
    InputChannelsFineTune to specify your remix values. Don't use both.
    """

    OutputChannels: Optional[_listOfOutputChannelMapping]


class RemixSettings(TypedDict, total=False):
    """Use Manual audio remixing to adjust audio levels for each audio channel
    in each output of your job. With audio remixing, you can output more or
    fewer audio channels than your input audio source provides.
    """

    AudioDescriptionAudioChannel: Optional[_integerMin1Max64]
    AudioDescriptionDataChannel: Optional[_integerMin1Max64]
    ChannelMapping: Optional[ChannelMapping]
    ChannelsIn: Optional[_integerMin1Max64]
    ChannelsOut: Optional[_integerMin1Max64]


class AudioNormalizationSettings(TypedDict, total=False):
    """Advanced audio normalization settings. Ignore these settings unless you
    need to comply with a loudness standard.
    """

    Algorithm: Optional[AudioNormalizationAlgorithm]
    AlgorithmControl: Optional[AudioNormalizationAlgorithmControl]
    CorrectionGateLevel: Optional[_integerMinNegative70Max0]
    LoudnessLogging: Optional[AudioNormalizationLoudnessLogging]
    PeakCalculation: Optional[AudioNormalizationPeakCalculation]
    TargetLkfs: Optional[_doubleMinNegative59Max0]
    TruePeakLimiterThreshold: Optional[_doubleMinNegative8Max0]


class AudioDescription(TypedDict, total=False):
    """Settings related to one audio tab on the MediaConvert console. In your
    job JSON, an instance of AudioDescription is equivalent to one audio tab
    in the console. Usually, one audio tab corresponds to one output audio
    track. Depending on how you set up your input audio selectors and
    whether you use audio selector groups, one audio tab can correspond to a
    group of output audio tracks.
    """

    AudioChannelTaggingSettings: Optional[AudioChannelTaggingSettings]
    AudioNormalizationSettings: Optional[AudioNormalizationSettings]
    AudioSourceName: Optional[_stringMax2048]
    AudioType: Optional[_integerMin0Max255]
    AudioTypeControl: Optional[AudioTypeControl]
    CodecSettings: Optional[AudioCodecSettings]
    CustomLanguageCode: Optional[_stringPatternAZaZ23AZaZ09]
    LanguageCode: Optional[LanguageCode]
    LanguageCodeControl: Optional[AudioLanguageCodeControl]
    RemixSettings: Optional[RemixSettings]
    StreamName: Optional[_stringPatternWS]


class FrameRate(TypedDict, total=False):
    """The frame rate of the video or audio track."""

    Denominator: Optional[_integer]
    Numerator: Optional[_integer]


_long = int


class AudioProperties(TypedDict, total=False):
    """Details about the media file's audio track."""

    BitDepth: Optional[_integer]
    BitRate: Optional[_long]
    Channels: Optional[_integer]
    FrameRate: Optional[FrameRate]
    LanguageCode: Optional[_string]
    SampleRate: Optional[_integer]


_listOf__integerMin1Max2147483647 = List[_integerMin1Max2147483647]


class HlsRenditionGroupSettings(TypedDict, total=False):
    """Settings specific to audio sources in an HLS alternate rendition group.
    Specify the properties (renditionGroupId, renditionName or
    renditionLanguageCode) to identify the unique audio track among the
    alternative rendition groups present in the HLS manifest. If no unique
    track is found, or multiple tracks match the properties provided, the
    job fails. If no properties in hlsRenditionGroupSettings are specified,
    the default audio track within the video segment is chosen. If there is
    no audio within video segment, the alternative audio with DEFAULT=YES is
    chosen instead.
    """

    RenditionGroupId: Optional[_string]
    RenditionLanguageCode: Optional[LanguageCode]
    RenditionName: Optional[_string]


class AudioSelector(TypedDict, total=False):
    """Use Audio selectors to specify a track or set of tracks from the input
    that you will use in your outputs. You can use multiple Audio selectors
    per input.
    """

    AudioDurationCorrection: Optional[AudioDurationCorrection]
    CustomLanguageCode: Optional[_stringMin3Max3PatternAZaZ3]
    DefaultSelection: Optional[AudioDefaultSelection]
    ExternalAudioFileInput: Optional[_stringPatternS3Https]
    HlsRenditionGroupSettings: Optional[HlsRenditionGroupSettings]
    LanguageCode: Optional[LanguageCode]
    Offset: Optional[_integerMinNegative2147483648Max2147483647]
    Pids: Optional[_listOf__integerMin1Max2147483647]
    ProgramSelection: Optional[_integerMin0Max8]
    RemixSettings: Optional[RemixSettings]
    SelectorType: Optional[AudioSelectorType]
    Tracks: Optional[_listOf__integerMin1Max2147483647]


_listOf__stringMin1 = List[_stringMin1]


class AudioSelectorGroup(TypedDict, total=False):
    """Use audio selector groups to combine multiple sidecar audio inputs so
    that you can assign them to a single output audio tab. Note that, if
    you're working with embedded audio, it's simpler to assign multiple
    input tracks into a single audio selector rather than use an audio
    selector group.
    """

    AudioSelectorNames: Optional[_listOf__stringMin1]


class MinTopRenditionSize(TypedDict, total=False):
    """Use Min top rendition size to specify a minimum size for the highest
    resolution in your ABR stack. \\* The highest resolution in your ABR
    stack will be equal to or greater than the value that you enter. For
    example: If you specify 1280x720 the highest resolution in your ABR
    stack will be equal to or greater than 1280x720. \\* If you specify a
    value for Max resolution, the value that you specify for Min top
    rendition size must be less than, or equal to, Max resolution.
    """

    Height: Optional[_integerMin32Max8192]
    Width: Optional[_integerMin32Max8192]


class MinBottomRenditionSize(TypedDict, total=False):
    """Use Min bottom rendition size to specify a minimum size for the lowest
    resolution in your ABR stack. \\* The lowest resolution in your ABR stack
    will be equal to or greater than the value that you enter. For example:
    If you specify 640x360 the lowest resolution in your ABR stack will be
    equal to or greater than to 640x360. \\* If you specify a Min top
    rendition size rule, the value that you specify for Min bottom rendition
    size must be less than, or equal to, Min top rendition size.
    """

    Height: Optional[_integerMin32Max8192]
    Width: Optional[_integerMin32Max8192]


class ForceIncludeRenditionSize(TypedDict, total=False):
    """Use Force include renditions to specify one or more resolutions to
    include your ABR stack. \\* (Recommended) To optimize automated ABR,
    specify as few resolutions as possible. \\* (Required) The number of
    resolutions that you specify must be equal to, or less than, the Max
    renditions setting. \\* If you specify a Min top rendition size rule,
    specify at least one resolution that is equal to, or greater than, Min
    top rendition size. \\* If you specify a Min bottom rendition size rule,
    only specify resolutions that are equal to, or greater than, Min bottom
    rendition size. \\* If you specify a Force include renditions rule, do
    not specify a separate rule for Allowed renditions. \\* Note: The ABR
    stack may include other resolutions that you do not specify here,
    depending on the Max renditions setting.
    """

    Height: Optional[_integerMin32Max8192]
    Width: Optional[_integerMin32Max8192]


_listOfForceIncludeRenditionSize = List[ForceIncludeRenditionSize]
_listOfAllowedRenditionSize = List[AllowedRenditionSize]


class AutomatedAbrRule(TypedDict, total=False):
    """Specify one or more Automated ABR rule types. Note: Force include and
    Allowed renditions are mutually exclusive.
    """

    AllowedRenditions: Optional[_listOfAllowedRenditionSize]
    ForceIncludeRenditions: Optional[_listOfForceIncludeRenditionSize]
    MinBottomRenditionSize: Optional[MinBottomRenditionSize]
    MinTopRenditionSize: Optional[MinTopRenditionSize]
    Type: Optional[RuleType]


_listOfAutomatedAbrRule = List[AutomatedAbrRule]


class AutomatedAbrSettings(TypedDict, total=False):
    """Use automated ABR to have MediaConvert set up the renditions in your ABR
    package for you automatically, based on characteristics of your input
    video. This feature optimizes video quality while minimizing the overall
    size of your ABR package.
    """

    MaxAbrBitrate: Optional[_integerMin100000Max100000000]
    MaxQualityLevel: Optional[_doubleMin1Max10]
    MaxRenditions: Optional[_integerMin3Max15]
    MinAbrBitrate: Optional[_integerMin100000Max100000000]
    Rules: Optional[_listOfAutomatedAbrRule]


class AutomatedEncodingSettings(TypedDict, total=False):
    """Use automated encoding to have MediaConvert choose your encoding
    settings for you, based on characteristics of your input video.
    """

    AbrSettings: Optional[AutomatedAbrSettings]


class Av1QvbrSettings(TypedDict, total=False):
    """Settings for quality-defined variable bitrate encoding with the AV1
    codec. Use these settings only when you set QVBR for Rate control mode.
    """

    QvbrQualityLevel: Optional[_integerMin1Max10]
    QvbrQualityLevelFineTune: Optional[_doubleMin0Max1]


_listOfFrameMetricType = List[FrameMetricType]


class Av1Settings(TypedDict, total=False):
    """Required when you set Codec, under VideoDescription>CodecSettings to the
    value AV1.
    """

    AdaptiveQuantization: Optional[Av1AdaptiveQuantization]
    BitDepth: Optional[Av1BitDepth]
    FilmGrainSynthesis: Optional[Av1FilmGrainSynthesis]
    FramerateControl: Optional[Av1FramerateControl]
    FramerateConversionAlgorithm: Optional[Av1FramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max2147483647]
    FramerateNumerator: Optional[_integerMin1Max2147483647]
    GopSize: Optional[_doubleMin0]
    MaxBitrate: Optional[_integerMin1000Max1152000000]
    NumberBFramesBetweenReferenceFrames: Optional[_integerMin0Max15]
    PerFrameMetrics: Optional[_listOfFrameMetricType]
    QvbrSettings: Optional[Av1QvbrSettings]
    RateControlMode: Optional[Av1RateControlMode]
    Slices: Optional[_integerMin1Max32]
    SpatialAdaptiveQuantization: Optional[Av1SpatialAdaptiveQuantization]


class AvailBlanking(TypedDict, total=False):
    """Use ad avail blanking settings to specify your output content during
    SCTE-35 triggered ad avails. You can blank your video or overlay it with
    an image. MediaConvert also removes any audio and embedded captions
    during the ad avail. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/ad-avail-blanking.html.
    """

    AvailBlankingImage: Optional[_stringMin14PatternS3BmpBMPPngPNGHttpsBmpBMPPngPNG]


class AvcIntraUhdSettings(TypedDict, total=False):
    """Optional when you set AVC-Intra class to Class 4K/2K. When you set
    AVC-Intra class to a different value, this object isn't allowed.
    """

    QualityTuningLevel: Optional[AvcIntraUhdQualityTuningLevel]


class AvcIntraSettings(TypedDict, total=False):
    """Required when you choose AVC-Intra for your output video codec. For more
    information about the AVC-Intra settings, see the relevant
    specification. For detailed information about SD and HD in AVC-Intra,
    see https://ieeexplore.ieee.org/document/7290936. For information about
    4K/2K in AVC-Intra, see
    https://pro-av.panasonic.net/en/avc-ultra/AVC-ULTRAoverview.pdf.
    """

    AvcIntraClass: Optional[AvcIntraClass]
    AvcIntraUhdSettings: Optional[AvcIntraUhdSettings]
    FramerateControl: Optional[AvcIntraFramerateControl]
    FramerateConversionAlgorithm: Optional[AvcIntraFramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max1001]
    FramerateNumerator: Optional[_integerMin24Max60000]
    InterlaceMode: Optional[AvcIntraInterlaceMode]
    PerFrameMetrics: Optional[_listOfFrameMetricType]
    ScanTypeConversionMode: Optional[AvcIntraScanTypeConversionMode]
    SlowPal: Optional[AvcIntraSlowPal]
    Telecine: Optional[AvcIntraTelecine]


class BandwidthReductionFilter(TypedDict, total=False):
    """The Bandwidth reduction filter increases the video quality of your
    output relative to its bitrate. Use to lower the bitrate of your
    constant quality QVBR output, with little or no perceptual decrease in
    quality. Or, use to increase the video quality of outputs with other
    rate control modes relative to the bitrate that you specify. Bandwidth
    reduction increases further when your input is low quality or noisy.
    Outputs that use this feature incur pro-tier pricing. When you include
    Bandwidth reduction filter, you cannot include the Noise reducer
    preprocessor.
    """

    Sharpening: Optional[BandwidthReductionFilterSharpening]
    Strength: Optional[BandwidthReductionFilterStrength]


class BurninDestinationSettings(TypedDict, total=False):
    """Burn-in is a captions delivery method, rather than a captions format.
    Burn-in writes the captions directly on your video frames, replacing
    pixels of video content with the captions. Set up burn-in captions in
    the same output as your video. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/burn-in-output-captions.html.
    """

    Alignment: Optional[BurninSubtitleAlignment]
    ApplyFontColor: Optional[BurninSubtitleApplyFontColor]
    BackgroundColor: Optional[BurninSubtitleBackgroundColor]
    BackgroundOpacity: Optional[_integerMin0Max255]
    FallbackFont: Optional[BurninSubtitleFallbackFont]
    FontColor: Optional[BurninSubtitleFontColor]
    FontFileBold: Optional[_stringPatternS3TtfHttpsTtf]
    FontFileBoldItalic: Optional[_string]
    FontFileItalic: Optional[_stringPatternS3TtfHttpsTtf]
    FontFileRegular: Optional[_stringPatternS3TtfHttpsTtf]
    FontOpacity: Optional[_integerMin0Max255]
    FontResolution: Optional[_integerMin96Max600]
    FontScript: Optional[FontScript]
    FontSize: Optional[_integerMin0Max96]
    HexFontColor: Optional[_stringMin6Max8Pattern09aFAF609aFAF2]
    OutlineColor: Optional[BurninSubtitleOutlineColor]
    OutlineSize: Optional[_integerMin0Max10]
    RemoveRubyReserveAttributes: Optional[RemoveRubyReserveAttributes]
    ShadowColor: Optional[BurninSubtitleShadowColor]
    ShadowOpacity: Optional[_integerMin0Max255]
    ShadowXOffset: Optional[_integerMinNegative2147483648Max2147483647]
    ShadowYOffset: Optional[_integerMinNegative2147483648Max2147483647]
    StylePassthrough: Optional[BurnInSubtitleStylePassthrough]
    TeletextSpacing: Optional[BurninSubtitleTeletextSpacing]
    XPosition: Optional[_integerMin0Max2147483647]
    YPosition: Optional[_integerMin0Max2147483647]


class CancelJobRequest(ServiceRequest):
    Id: _string


class CancelJobResponse(TypedDict, total=False):
    pass


class WebvttDestinationSettings(TypedDict, total=False):
    """Settings related to WebVTT captions. WebVTT is a sidecar format that
    holds captions in a file that is separate from the video container. Set
    up sidecar captions in the same output group, but different output from
    your video. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html.
    """

    Accessibility: Optional[WebvttAccessibilitySubs]
    StylePassthrough: Optional[WebvttStylePassthrough]


class TtmlDestinationSettings(TypedDict, total=False):
    """Settings related to TTML captions. TTML is a sidecar format that holds
    captions in a file that is separate from the video container. Set up
    sidecar captions in the same output group, but different output from
    your video. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html.
    """

    StylePassthrough: Optional[TtmlStylePassthrough]


_listOfTeletextPageType = List[TeletextPageType]


class TeletextDestinationSettings(TypedDict, total=False):
    """Settings related to teletext captions. Set up teletext captions in the
    same output as your video. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/teletext-output-captions.html.
    """

    PageNumber: Optional[_stringMin3Max3Pattern1809aFAF09aEAE]
    PageTypes: Optional[_listOfTeletextPageType]


class SrtDestinationSettings(TypedDict, total=False):
    """Settings related to SRT captions. SRT is a sidecar format that holds
    captions in a file that is separate from the video container. Set up
    sidecar captions in the same output group, but different output from
    your video.
    """

    StylePassthrough: Optional[SrtStylePassthrough]


class SccDestinationSettings(TypedDict, total=False):
    """Settings related to SCC captions. SCC is a sidecar format that holds
    captions in a file that is separate from the video container. Set up
    sidecar captions in the same output group, but different output from
    your video. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/scc-srt-output-captions.html.
    """

    Framerate: Optional[SccDestinationFramerate]


class ImscDestinationSettings(TypedDict, total=False):
    """Settings related to IMSC captions. IMSC is a sidecar format that holds
    captions in a file that is separate from the video container. Set up
    sidecar captions in the same output group, but different output from
    your video. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html.
    """

    Accessibility: Optional[ImscAccessibilitySubs]
    StylePassthrough: Optional[ImscStylePassthrough]


class EmbeddedDestinationSettings(TypedDict, total=False):
    """Settings related to CEA/EIA-608 and CEA/EIA-708 (also called embedded or
    ancillary) captions. Set up embedded captions in the same output as your
    video. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/embedded-output-captions.html.
    """

    Destination608ChannelNumber: Optional[_integerMin1Max4]
    Destination708ServiceNumber: Optional[_integerMin1Max6]


class DvbSubDestinationSettings(TypedDict, total=False):
    """Settings related to DVB-Sub captions. Set up DVB-Sub captions in the
    same output as your video. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html.
    """

    Alignment: Optional[DvbSubtitleAlignment]
    ApplyFontColor: Optional[DvbSubtitleApplyFontColor]
    BackgroundColor: Optional[DvbSubtitleBackgroundColor]
    BackgroundOpacity: Optional[_integerMin0Max255]
    DdsHandling: Optional[DvbddsHandling]
    DdsXCoordinate: Optional[_integerMin0Max2147483647]
    DdsYCoordinate: Optional[_integerMin0Max2147483647]
    FallbackFont: Optional[DvbSubSubtitleFallbackFont]
    FontColor: Optional[DvbSubtitleFontColor]
    FontFileBold: Optional[_stringPatternS3TtfHttpsTtf]
    FontFileBoldItalic: Optional[_stringPatternS3TtfHttpsTtf]
    FontFileItalic: Optional[_stringPatternS3TtfHttpsTtf]
    FontFileRegular: Optional[_stringPatternS3TtfHttpsTtf]
    FontOpacity: Optional[_integerMin0Max255]
    FontResolution: Optional[_integerMin96Max600]
    FontScript: Optional[FontScript]
    FontSize: Optional[_integerMin0Max96]
    Height: Optional[_integerMin1Max2147483647]
    HexFontColor: Optional[_stringMin6Max8Pattern09aFAF609aFAF2]
    OutlineColor: Optional[DvbSubtitleOutlineColor]
    OutlineSize: Optional[_integerMin0Max10]
    ShadowColor: Optional[DvbSubtitleShadowColor]
    ShadowOpacity: Optional[_integerMin0Max255]
    ShadowXOffset: Optional[_integerMinNegative2147483648Max2147483647]
    ShadowYOffset: Optional[_integerMinNegative2147483648Max2147483647]
    StylePassthrough: Optional[DvbSubtitleStylePassthrough]
    SubtitlingType: Optional[DvbSubtitlingType]
    TeletextSpacing: Optional[DvbSubtitleTeletextSpacing]
    Width: Optional[_integerMin1Max2147483647]
    XPosition: Optional[_integerMin0Max2147483647]
    YPosition: Optional[_integerMin0Max2147483647]


class CaptionDestinationSettings(TypedDict, total=False):
    """Settings related to one captions tab on the MediaConvert console.
    Usually, one captions tab corresponds to one output captions track.
    Depending on your output captions format, one tab might correspond to a
    set of output captions tracks. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html.
    """

    BurninDestinationSettings: Optional[BurninDestinationSettings]
    DestinationType: Optional[CaptionDestinationType]
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettings]
    EmbeddedDestinationSettings: Optional[EmbeddedDestinationSettings]
    ImscDestinationSettings: Optional[ImscDestinationSettings]
    SccDestinationSettings: Optional[SccDestinationSettings]
    SrtDestinationSettings: Optional[SrtDestinationSettings]
    TeletextDestinationSettings: Optional[TeletextDestinationSettings]
    TtmlDestinationSettings: Optional[TtmlDestinationSettings]
    WebvttDestinationSettings: Optional[WebvttDestinationSettings]


class CaptionDescription(TypedDict, total=False):
    """This object holds groups of settings related to captions for one output.
    For each output that has captions, include one instance of
    CaptionDescriptions.
    """

    CaptionSelectorName: Optional[_stringMin1]
    CustomLanguageCode: Optional[_stringPatternAZaZ23AZaZ]
    DestinationSettings: Optional[CaptionDestinationSettings]
    LanguageCode: Optional[LanguageCode]
    LanguageDescription: Optional[_string]


class CaptionDescriptionPreset(TypedDict, total=False):
    """Caption Description for preset"""

    CustomLanguageCode: Optional[_stringPatternAZaZ23AZaZ]
    DestinationSettings: Optional[CaptionDestinationSettings]
    LanguageCode: Optional[LanguageCode]
    LanguageDescription: Optional[_string]


class WebvttHlsSourceSettings(TypedDict, total=False):
    """Settings specific to WebVTT sources in HLS alternative rendition group.
    Specify the properties (renditionGroupId, renditionName or
    renditionLanguageCode) to identify the unique subtitle track among the
    alternative rendition groups present in the HLS manifest. If no unique
    track is found, or multiple tracks match the specified properties, the
    job fails. If there is only one subtitle track in the rendition group,
    the settings can be left empty and the default subtitle track will be
    chosen. If your caption source is a sidecar file, use FileSourceSettings
    instead of WebvttHlsSourceSettings.
    """

    RenditionGroupId: Optional[_string]
    RenditionLanguageCode: Optional[LanguageCode]
    RenditionName: Optional[_string]


class TrackSourceSettings(TypedDict, total=False):
    """Settings specific to caption sources that are specified by track number.
    Currently, this is only IMSC captions in an IMF package. If your caption
    source is IMSC 1.1 in a separate xml file, use FileSourceSettings
    instead of TrackSourceSettings.
    """

    TrackNumber: Optional[_integerMin1Max2147483647]


class TeletextSourceSettings(TypedDict, total=False):
    """Settings specific to Teletext caption sources, including Page number."""

    PageNumber: Optional[_stringMin3Max3Pattern1809aFAF09aEAE]


class CaptionSourceFramerate(TypedDict, total=False):
    """Ignore this setting unless your input captions format is SCC. To have
    the service compensate for differing frame rates between your input
    captions and input video, specify the frame rate of the captions file.
    Specify this value as a fraction. For example, you might specify 24 / 1
    for 24 fps, 25 / 1 for 25 fps, 24000 / 1001 for 23.976 fps, or 30000 /
    1001 for 29.97 fps.
    """

    FramerateDenominator: Optional[_integerMin1Max1001]
    FramerateNumerator: Optional[_integerMin1Max60000]


class FileSourceSettings(TypedDict, total=False):
    """If your input captions are SCC, SMI, SRT, STL, TTML, WebVTT, or IMSC 1.1
    in an xml file, specify the URI of the input caption source file. If
    your caption source is IMSC in an IMF package, use TrackSourceSettings
    instead of FileSoureSettings.
    """

    ByteRateLimit: Optional[CaptionSourceByteRateLimit]
    Convert608To708: Optional[FileSourceConvert608To708]
    ConvertPaintToPop: Optional[CaptionSourceConvertPaintOnToPopOn]
    Framerate: Optional[CaptionSourceFramerate]
    SourceFile: Optional[
        _stringMin14PatternS3SccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTTHttpsSccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTT
    ]
    TimeDelta: Optional[_integerMinNegative2147483648Max2147483647]
    TimeDeltaUnits: Optional[FileSourceTimeDeltaUnits]
    UpconvertSTLToTeletext: Optional[CaptionSourceUpconvertSTLToTeletext]


class EmbeddedSourceSettings(TypedDict, total=False):
    """Settings for embedded captions Source"""

    Convert608To708: Optional[EmbeddedConvert608To708]
    Source608ChannelNumber: Optional[_integerMin1Max4]
    Source608TrackNumber: Optional[_integerMin1Max1]
    TerminateCaptions: Optional[EmbeddedTerminateCaptions]


class DvbSubSourceSettings(TypedDict, total=False):
    """DVB Sub Source Settings"""

    Pid: Optional[_integerMin1Max2147483647]


class CaptionSourceSettings(TypedDict, total=False):
    """If your input captions are SCC, TTML, STL, SMI, SRT, or IMSC in an xml
    file, specify the URI of the input captions source file. If your input
    captions are IMSC in an IMF package, use TrackSourceSettings instead of
    FileSoureSettings.
    """

    AncillarySourceSettings: Optional[AncillarySourceSettings]
    DvbSubSourceSettings: Optional[DvbSubSourceSettings]
    EmbeddedSourceSettings: Optional[EmbeddedSourceSettings]
    FileSourceSettings: Optional[FileSourceSettings]
    SourceType: Optional[CaptionSourceType]
    TeletextSourceSettings: Optional[TeletextSourceSettings]
    TrackSourceSettings: Optional[TrackSourceSettings]
    WebvttHlsSourceSettings: Optional[WebvttHlsSourceSettings]


class CaptionSelector(TypedDict, total=False):
    """Use captions selectors to specify the captions data from your input that
    you use in your outputs. You can use up to 100 captions selectors per
    input.
    """

    CustomLanguageCode: Optional[_stringMin3Max3PatternAZaZ3]
    LanguageCode: Optional[LanguageCode]
    SourceSettings: Optional[CaptionSourceSettings]


class ClipLimits(TypedDict, total=False):
    """Specify YUV limits and RGB tolerances when you set Sample range
    conversion to Limited range clip.
    """

    MaximumRGBTolerance: Optional[_integerMin90Max105]
    MaximumYUV: Optional[_integerMin920Max1023]
    MinimumRGBTolerance: Optional[_integerMinNegative5Max10]
    MinimumYUV: Optional[_integerMin0Max128]


class CmafAdditionalManifest(TypedDict, total=False):
    """Specify the details for each pair of HLS and DASH additional manifests
    that you want the service to generate for this CMAF output group. Each
    pair of manifests can reference a different subset of outputs in the
    group.
    """

    ManifestNameModifier: Optional[_stringMin1]
    SelectedOutputs: Optional[_listOf__stringMin1]


class StaticKeyProvider(TypedDict, total=False):
    """Use these settings to set up encryption with a static key provider."""

    KeyFormat: Optional[_stringPatternIdentityAZaZ26AZaZ09163]
    KeyFormatVersions: Optional[_stringPatternDD]
    StaticKeyValue: Optional[_stringPatternAZaZ0932]
    Url: Optional[_string]


_listOf__stringMin36Max36Pattern09aFAF809aFAF409aFAF409aFAF409aFAF12 = List[
    _stringMin36Max36Pattern09aFAF809aFAF409aFAF409aFAF409aFAF12
]


class EncryptionContractConfiguration(TypedDict, total=False):
    """Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses
    when encrypting your output. For more information, see:
    https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html
    To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0
    video preset and a SPEKE v2.0 audio preset.
    """

    SpekeAudioPreset: Optional[PresetSpeke20Audio]
    SpekeVideoPreset: Optional[PresetSpeke20Video]


class SpekeKeyProviderCmaf(TypedDict, total=False):
    """If your output group type is CMAF, use these settings when doing DRM
    encryption with a SPEKE-compliant key provider. If your output group
    type is HLS, DASH, or Microsoft Smooth, use the SpekeKeyProvider
    settings instead.
    """

    CertificateArn: Optional[_stringPatternArnAwsUsGovAcm]
    DashSignaledSystemIds: Optional[
        _listOf__stringMin36Max36Pattern09aFAF809aFAF409aFAF409aFAF409aFAF12
    ]
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration]
    HlsSignaledSystemIds: Optional[
        _listOf__stringMin36Max36Pattern09aFAF809aFAF409aFAF409aFAF409aFAF12
    ]
    ResourceId: Optional[_stringPatternW]
    Url: Optional[_stringPatternHttpsD]


class CmafEncryptionSettings(TypedDict, total=False):
    """Settings for CMAF encryption"""

    ConstantInitializationVector: Optional[_stringMin32Max32Pattern09aFAF32]
    EncryptionMethod: Optional[CmafEncryptionType]
    InitializationVectorInManifest: Optional[CmafInitializationVectorInManifest]
    SpekeKeyProvider: Optional[SpekeKeyProviderCmaf]
    StaticKeyProvider: Optional[StaticKeyProvider]
    Type: Optional[CmafKeyProviderType]


class CmafImageBasedTrickPlaySettings(TypedDict, total=False):
    """Tile and thumbnail settings applicable when imageBasedTrickPlay is
    ADVANCED
    """

    IntervalCadence: Optional[CmafIntervalCadence]
    ThumbnailHeight: Optional[_integerMin2Max4096]
    ThumbnailInterval: Optional[_doubleMin0Max2147483647]
    ThumbnailWidth: Optional[_integerMin8Max4096]
    TileHeight: Optional[_integerMin1Max2048]
    TileWidth: Optional[_integerMin1Max512]


class S3EncryptionSettings(TypedDict, total=False):
    """Settings for how your job outputs are encrypted as they are uploaded to
    Amazon S3.
    """

    EncryptionType: Optional[S3ServerSideEncryptionType]
    KmsEncryptionContext: Optional[_stringPatternAZaZ0902]
    KmsKeyArn: Optional[
        _stringPatternArnAwsUsGovCnKmsAZ26EastWestCentralNorthSouthEastWest1912D12KeyAFAF098AFAF094AFAF094AFAF094AFAF0912MrkAFAF0932
    ]


class S3DestinationAccessControl(TypedDict, total=False):
    """Optional. Have MediaConvert automatically apply Amazon S3 access control
    for the outputs in this output group. When you don't use this setting,
    S3 automatically applies the default access control list PRIVATE.
    """

    CannedAcl: Optional[S3ObjectCannedAcl]


class S3DestinationSettings(TypedDict, total=False):
    """Settings associated with S3 destination"""

    AccessControl: Optional[S3DestinationAccessControl]
    Encryption: Optional[S3EncryptionSettings]
    StorageClass: Optional[S3StorageClass]


class DestinationSettings(TypedDict, total=False):
    """Settings associated with the destination. Will vary based on the type of
    destination
    """

    S3Settings: Optional[S3DestinationSettings]


_listOfCmafAdditionalManifest = List[CmafAdditionalManifest]


class CmafGroupSettings(TypedDict, total=False):
    """Settings related to your CMAF output package. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html.
    """

    AdditionalManifests: Optional[_listOfCmafAdditionalManifest]
    BaseUrl: Optional[_string]
    ClientCache: Optional[CmafClientCache]
    CodecSpecification: Optional[CmafCodecSpecification]
    DashIFrameTrickPlayNameModifier: Optional[_stringMin1Max256]
    DashManifestStyle: Optional[DashManifestStyle]
    Destination: Optional[_stringPatternS3]
    DestinationSettings: Optional[DestinationSettings]
    Encryption: Optional[CmafEncryptionSettings]
    FragmentLength: Optional[_integerMin1Max2147483647]
    ImageBasedTrickPlay: Optional[CmafImageBasedTrickPlay]
    ImageBasedTrickPlaySettings: Optional[CmafImageBasedTrickPlaySettings]
    ManifestCompression: Optional[CmafManifestCompression]
    ManifestDurationFormat: Optional[CmafManifestDurationFormat]
    MinBufferTime: Optional[_integerMin0Max2147483647]
    MinFinalSegmentLength: Optional[_doubleMin0Max2147483647]
    MpdManifestBandwidthType: Optional[CmafMpdManifestBandwidthType]
    MpdProfile: Optional[CmafMpdProfile]
    PtsOffsetHandlingForBFrames: Optional[CmafPtsOffsetHandlingForBFrames]
    SegmentControl: Optional[CmafSegmentControl]
    SegmentLength: Optional[_integerMin1Max2147483647]
    SegmentLengthControl: Optional[CmafSegmentLengthControl]
    StreamInfResolution: Optional[CmafStreamInfResolution]
    TargetDurationCompatibilityMode: Optional[CmafTargetDurationCompatibilityMode]
    VideoCompositionOffsets: Optional[CmafVideoCompositionOffsets]
    WriteDashManifest: Optional[CmafWriteDASHManifest]
    WriteHlsManifest: Optional[CmafWriteHLSManifest]
    WriteSegmentTimelineInRepresentation: Optional[CmafWriteSegmentTimelineInRepresentation]


class CmfcSettings(TypedDict, total=False):
    """These settings relate to the fragmented MP4 container for the segments
    in your CMAF outputs.
    """

    AudioDuration: Optional[CmfcAudioDuration]
    AudioGroupId: Optional[_string]
    AudioRenditionSets: Optional[_string]
    AudioTrackType: Optional[CmfcAudioTrackType]
    DescriptiveVideoServiceFlag: Optional[CmfcDescriptiveVideoServiceFlag]
    IFrameOnlyManifest: Optional[CmfcIFrameOnlyManifest]
    KlvMetadata: Optional[CmfcKlvMetadata]
    ManifestMetadataSignaling: Optional[CmfcManifestMetadataSignaling]
    Scte35Esam: Optional[CmfcScte35Esam]
    Scte35Source: Optional[CmfcScte35Source]
    TimedMetadata: Optional[CmfcTimedMetadata]
    TimedMetadataBoxVersion: Optional[CmfcTimedMetadataBoxVersion]
    TimedMetadataSchemeIdUri: Optional[_stringMax1000]
    TimedMetadataValue: Optional[_stringMax1000]


class ColorConversion3DLUTSetting(TypedDict, total=False):
    """Custom 3D lut settings"""

    FileInput: Optional[_stringMin14PatternS3CubeCUBEHttpsCubeCUBE]
    InputColorSpace: Optional[ColorSpace]
    InputMasteringLuminance: Optional[_integerMin0Max2147483647]
    OutputColorSpace: Optional[ColorSpace]
    OutputMasteringLuminance: Optional[_integerMin0Max2147483647]


class Hdr10Metadata(TypedDict, total=False):
    """Use these settings to specify static color calibration metadata, as
    defined by SMPTE ST 2086. These values don't affect the pixel values
    that are encoded in the video stream. They are intended to help the
    downstream video player display content in a way that reflects the
    intentions of the the content creator.
    """

    BluePrimaryX: Optional[_integerMin0Max50000]
    BluePrimaryY: Optional[_integerMin0Max50000]
    GreenPrimaryX: Optional[_integerMin0Max50000]
    GreenPrimaryY: Optional[_integerMin0Max50000]
    MaxContentLightLevel: Optional[_integerMin0Max65535]
    MaxFrameAverageLightLevel: Optional[_integerMin0Max65535]
    MaxLuminance: Optional[_integerMin0Max2147483647]
    MinLuminance: Optional[_integerMin0Max2147483647]
    RedPrimaryX: Optional[_integerMin0Max50000]
    RedPrimaryY: Optional[_integerMin0Max50000]
    WhitePointX: Optional[_integerMin0Max50000]
    WhitePointY: Optional[_integerMin0Max50000]


class ColorCorrector(TypedDict, total=False):
    """Settings for color correction."""

    Brightness: Optional[_integerMin1Max100]
    ClipLimits: Optional[ClipLimits]
    ColorSpaceConversion: Optional[ColorSpaceConversion]
    Contrast: Optional[_integerMin1Max100]
    Hdr10Metadata: Optional[Hdr10Metadata]
    HdrToSdrToneMapper: Optional[HDRToSDRToneMapper]
    Hue: Optional[_integerMinNegative180Max180]
    MaxLuminance: Optional[_integerMin0Max2147483647]
    SampleRangeConversion: Optional[SampleRangeConversion]
    Saturation: Optional[_integerMin1Max100]
    SdrReferenceWhiteLevel: Optional[_integerMin100Max1000]


class VideoProperties(TypedDict, total=False):
    """Details about the media file's video track."""

    BitDepth: Optional[_integer]
    BitRate: Optional[_long]
    ColorPrimaries: Optional[ColorPrimaries]
    FrameRate: Optional[FrameRate]
    Height: Optional[_integer]
    MatrixCoefficients: Optional[MatrixCoefficients]
    TransferCharacteristics: Optional[TransferCharacteristics]
    Width: Optional[_integer]


class DataProperties(TypedDict, total=False):
    """Details about the media file's data track."""

    LanguageCode: Optional[_string]


class Track(TypedDict, total=False):
    """Details about each track (video, audio, or data) in the media file."""

    AudioProperties: Optional[AudioProperties]
    Codec: Optional[Codec]
    DataProperties: Optional[DataProperties]
    Duration: Optional[_double]
    Index: Optional[_integer]
    TrackType: Optional[TrackType]
    VideoProperties: Optional[VideoProperties]


_listOfTrack = List[Track]


class Container(TypedDict, total=False):
    """The container of your media file. This information helps you understand
    the overall structure and details of your media, including format,
    duration, and track layout.
    """

    Duration: Optional[_double]
    Format: Optional[Format]
    Tracks: Optional[_listOfTrack]


class MxfXavcProfileSettings(TypedDict, total=False):
    """Specify the XAVC profile settings for MXF outputs when you set your MXF
    profile to XAVC.
    """

    DurationMode: Optional[MxfXavcDurationMode]
    MaxAncDataSize: Optional[_integerMin0Max2147483647]


class MxfSettings(TypedDict, total=False):
    """These settings relate to your MXF output container."""

    AfdSignaling: Optional[MxfAfdSignaling]
    Profile: Optional[MxfProfile]
    XavcProfileSettings: Optional[MxfXavcProfileSettings]


class MpdSettings(TypedDict, total=False):
    """These settings relate to the fragmented MP4 container for the segments
    in your DASH outputs.
    """

    AccessibilityCaptionHints: Optional[MpdAccessibilityCaptionHints]
    AudioDuration: Optional[MpdAudioDuration]
    CaptionContainerType: Optional[MpdCaptionContainerType]
    KlvMetadata: Optional[MpdKlvMetadata]
    ManifestMetadataSignaling: Optional[MpdManifestMetadataSignaling]
    Scte35Esam: Optional[MpdScte35Esam]
    Scte35Source: Optional[MpdScte35Source]
    TimedMetadata: Optional[MpdTimedMetadata]
    TimedMetadataBoxVersion: Optional[MpdTimedMetadataBoxVersion]
    TimedMetadataSchemeIdUri: Optional[_stringMax1000]
    TimedMetadataValue: Optional[_stringMax1000]


class Mp4Settings(TypedDict, total=False):
    """These settings relate to your MP4 output container. You can create audio
    only outputs with this container. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/supported-codecs-containers-audio-only.html#output-codecs-and-containers-supported-for-audio-only.
    """

    AudioDuration: Optional[CmfcAudioDuration]
    CslgAtom: Optional[Mp4CslgAtom]
    CttsVersion: Optional[_integerMin0Max1]
    FreeSpaceBox: Optional[Mp4FreeSpaceBox]
    MoovPlacement: Optional[Mp4MoovPlacement]
    Mp4MajorBrand: Optional[_string]


class MovSettings(TypedDict, total=False):
    """These settings relate to your QuickTime MOV output container."""

    ClapAtom: Optional[MovClapAtom]
    CslgAtom: Optional[MovCslgAtom]
    Mpeg2FourCCControl: Optional[MovMpeg2FourCCControl]
    PaddingControl: Optional[MovPaddingControl]
    Reference: Optional[MovReference]


_listOf__integerMin32Max8182 = List[_integerMin32Max8182]


class M3u8Settings(TypedDict, total=False):
    """These settings relate to the MPEG-2 transport stream (MPEG2-TS)
    container for the MPEG2-TS segments in your HLS outputs.
    """

    AudioDuration: Optional[M3u8AudioDuration]
    AudioFramesPerPes: Optional[_integerMin0Max2147483647]
    AudioPids: Optional[_listOf__integerMin32Max8182]
    AudioPtsOffsetDelta: Optional[_integerMinNegative10000Max10000]
    DataPTSControl: Optional[M3u8DataPtsControl]
    MaxPcrInterval: Optional[_integerMin0Max500]
    NielsenId3: Optional[M3u8NielsenId3]
    PatInterval: Optional[_integerMin0Max1000]
    PcrControl: Optional[M3u8PcrControl]
    PcrPid: Optional[_integerMin32Max8182]
    PmtInterval: Optional[_integerMin0Max1000]
    PmtPid: Optional[_integerMin32Max8182]
    PrivateMetadataPid: Optional[_integerMin32Max8182]
    ProgramNumber: Optional[_integerMin0Max65535]
    PtsOffset: Optional[_integerMin0Max3600]
    PtsOffsetMode: Optional[TsPtsOffset]
    Scte35Pid: Optional[_integerMin32Max8182]
    Scte35Source: Optional[M3u8Scte35Source]
    TimedMetadata: Optional[TimedMetadata]
    TimedMetadataPid: Optional[_integerMin32Max8182]
    TransportStreamId: Optional[_integerMin0Max65535]
    VideoPid: Optional[_integerMin32Max8182]


class M2tsScte35Esam(TypedDict, total=False):
    """Settings for SCTE-35 signals from ESAM. Include this in your job
    settings to put SCTE-35 markers in your HLS and transport stream outputs
    at the insertion points that you specify in an ESAM XML document.
    Provide the document in the setting SCC XML.
    """

    Scte35EsamPid: Optional[_integerMin32Max8182]


class DvbTdtSettings(TypedDict, total=False):
    """Use these settings to insert a DVB Time and Date Table (TDT) in the
    transport stream of this output.
    """

    TdtInterval: Optional[_integerMin1000Max30000]


class DvbSdtSettings(TypedDict, total=False):
    """Use these settings to insert a DVB Service Description Table (SDT) in
    the transport stream of this output.
    """

    OutputSdt: Optional[OutputSdt]
    SdtInterval: Optional[_integerMin25Max2000]
    ServiceName: Optional[_stringMin1Max256]
    ServiceProviderName: Optional[_stringMin1Max256]


class DvbNitSettings(TypedDict, total=False):
    """Use these settings to insert a DVB Network Information Table (NIT) in
    the transport stream of this output.
    """

    NetworkId: Optional[_integerMin0Max65535]
    NetworkName: Optional[_stringMin1Max256]
    NitInterval: Optional[_integerMin25Max10000]


class M2tsSettings(TypedDict, total=False):
    """MPEG-2 TS container settings. These apply to outputs in a File output
    group when the output's container is MPEG-2 Transport Stream (M2TS). In
    these assets, data is organized by the program map table (PMT). Each
    transport stream program contains subsets of data, including audio,
    video, and metadata. Each of these subsets of data has a numerical label
    called a packet identifier (PID). Each transport stream program
    corresponds to one MediaConvert output. The PMT lists the types of data
    in a program along with their PID. Downstream systems and players use
    the program map table to look up the PID for each type of data it
    accesses and then uses the PIDs to locate specific data within the
    asset.
    """

    AudioBufferModel: Optional[M2tsAudioBufferModel]
    AudioDuration: Optional[M2tsAudioDuration]
    AudioFramesPerPes: Optional[_integerMin0Max2147483647]
    AudioPids: Optional[_listOf__integerMin32Max8182]
    AudioPtsOffsetDelta: Optional[_integerMinNegative10000Max10000]
    Bitrate: Optional[_integerMin0Max2147483647]
    BufferModel: Optional[M2tsBufferModel]
    DataPTSControl: Optional[M2tsDataPtsControl]
    DvbNitSettings: Optional[DvbNitSettings]
    DvbSdtSettings: Optional[DvbSdtSettings]
    DvbSubPids: Optional[_listOf__integerMin32Max8182]
    DvbTdtSettings: Optional[DvbTdtSettings]
    DvbTeletextPid: Optional[_integerMin32Max8182]
    EbpAudioInterval: Optional[M2tsEbpAudioInterval]
    EbpPlacement: Optional[M2tsEbpPlacement]
    EsRateInPes: Optional[M2tsEsRateInPes]
    ForceTsVideoEbpOrder: Optional[M2tsForceTsVideoEbpOrder]
    FragmentTime: Optional[_doubleMin0]
    KlvMetadata: Optional[M2tsKlvMetadata]
    MaxPcrInterval: Optional[_integerMin0Max500]
    MinEbpInterval: Optional[_integerMin0Max10000]
    NielsenId3: Optional[M2tsNielsenId3]
    NullPacketBitrate: Optional[_doubleMin0]
    PatInterval: Optional[_integerMin0Max1000]
    PcrControl: Optional[M2tsPcrControl]
    PcrPid: Optional[_integerMin32Max8182]
    PmtInterval: Optional[_integerMin0Max1000]
    PmtPid: Optional[_integerMin32Max8182]
    PreventBufferUnderflow: Optional[M2tsPreventBufferUnderflow]
    PrivateMetadataPid: Optional[_integerMin32Max8182]
    ProgramNumber: Optional[_integerMin0Max65535]
    PtsOffset: Optional[_integerMin0Max3600]
    PtsOffsetMode: Optional[TsPtsOffset]
    RateMode: Optional[M2tsRateMode]
    Scte35Esam: Optional[M2tsScte35Esam]
    Scte35Pid: Optional[_integerMin32Max8182]
    Scte35Source: Optional[M2tsScte35Source]
    SegmentationMarkers: Optional[M2tsSegmentationMarkers]
    SegmentationStyle: Optional[M2tsSegmentationStyle]
    SegmentationTime: Optional[_doubleMin0]
    TimedMetadataPid: Optional[_integerMin32Max8182]
    TransportStreamId: Optional[_integerMin0Max65535]
    VideoPid: Optional[_integerMin32Max8182]


class F4vSettings(TypedDict, total=False):
    """Settings for F4v container"""

    MoovPlacement: Optional[F4vMoovPlacement]


class ContainerSettings(TypedDict, total=False):
    """Container specific settings."""

    CmfcSettings: Optional[CmfcSettings]
    Container: Optional[ContainerType]
    F4vSettings: Optional[F4vSettings]
    M2tsSettings: Optional[M2tsSettings]
    M3u8Settings: Optional[M3u8Settings]
    MovSettings: Optional[MovSettings]
    Mp4Settings: Optional[Mp4Settings]
    MpdSettings: Optional[MpdSettings]
    MxfSettings: Optional[MxfSettings]


_mapOf__string = Dict[_string, _string]


class Id3Insertion(TypedDict, total=False):
    """To insert ID3 tags in your output, specify two values. Use ID3 tag to
    specify the base 64 encoded string and use Timecode to specify the time
    when the tag should be inserted. To insert multiple ID3 tags in your
    output, create multiple instances of ID3 insertion.
    """

    Id3: Optional[_stringPatternAZaZ0902]
    Timecode: Optional[_stringPattern010920405090509092]


_listOfId3Insertion = List[Id3Insertion]


class TimedMetadataInsertion(TypedDict, total=False):
    """Insert user-defined custom ID3 metadata at timecodes that you specify.
    In each output that you want to include this metadata, you must set ID3
    metadata to Passthrough.
    """

    Id3Insertions: Optional[_listOfId3Insertion]


class TimecodeConfig(TypedDict, total=False):
    """These settings control how the service handles timecodes throughout the
    job. These settings don't affect input clipping.
    """

    Anchor: Optional[_stringPattern010920405090509092]
    Source: Optional[TimecodeSource]
    Start: Optional[_stringPattern010920405090509092]
    TimestampOffset: Optional[_stringPattern0940191020191209301]


class TimecodeBurnin(TypedDict, total=False):
    """Settings for burning the output timecode and specified prefix into the
    output.
    """

    FontSize: Optional[_integerMin10Max48]
    Position: Optional[TimecodeBurninPosition]
    Prefix: Optional[_stringPattern]


class NexGuardFileMarkerSettings(TypedDict, total=False):
    """For forensic video watermarking, MediaConvert supports Nagra NexGuard
    File Marker watermarking. MediaConvert supports both PreRelease Content
    (NGPR/G2) and OTT Streaming workflows.
    """

    License: Optional[_stringMin1Max100000]
    Payload: Optional[_integerMin0Max4194303]
    Preset: Optional[_stringMin1Max256]
    Strength: Optional[WatermarkingStrength]


class PartnerWatermarking(TypedDict, total=False):
    """If you work with a third party video watermarking partner, use the group
    of settings that correspond with your watermarking partner to include
    watermarks in your output.
    """

    NexguardFileMarkerSettings: Optional[NexGuardFileMarkerSettings]


class NoiseReducerTemporalFilterSettings(TypedDict, total=False):
    """Noise reducer filter settings for temporal filter."""

    AggressiveMode: Optional[_integerMin0Max4]
    PostTemporalSharpening: Optional[NoiseFilterPostTemporalSharpening]
    PostTemporalSharpeningStrength: Optional[NoiseFilterPostTemporalSharpeningStrength]
    Speed: Optional[_integerMinNegative1Max3]
    Strength: Optional[_integerMin0Max16]


class NoiseReducerSpatialFilterSettings(TypedDict, total=False):
    """Noise reducer filter settings for spatial filter."""

    PostFilterSharpenStrength: Optional[_integerMin0Max3]
    Speed: Optional[_integerMinNegative2Max3]
    Strength: Optional[_integerMin0Max16]


class NoiseReducerFilterSettings(TypedDict, total=False):
    """Settings for a noise reducer filter"""

    Strength: Optional[_integerMin0Max3]


class NoiseReducer(TypedDict, total=False):
    """Enable the Noise reducer feature to remove noise from your video output
    if necessary. Enable or disable this feature for each output
    individually. This setting is disabled by default. When you enable Noise
    reducer, you must also select a value for Noise reducer filter. For AVC
    outputs, when you include Noise reducer, you cannot include the
    Bandwidth reduction filter.
    """

    Filter: Optional[NoiseReducerFilter]
    FilterSettings: Optional[NoiseReducerFilterSettings]
    SpatialFilterSettings: Optional[NoiseReducerSpatialFilterSettings]
    TemporalFilterSettings: Optional[NoiseReducerTemporalFilterSettings]


class InsertableImage(TypedDict, total=False):
    """These settings apply to a specific graphic overlay. You can include
    multiple overlays in your job.
    """

    Duration: Optional[_integerMin0Max2147483647]
    FadeIn: Optional[_integerMin0Max2147483647]
    FadeOut: Optional[_integerMin0Max2147483647]
    Height: Optional[_integerMin0Max2147483647]
    ImageInserterInput: Optional[_stringMin14PatternS3BmpBMPPngPNGTgaTGAHttpsBmpBMPPngPNGTgaTGA]
    ImageX: Optional[_integerMin0Max2147483647]
    ImageY: Optional[_integerMin0Max2147483647]
    Layer: Optional[_integerMin0Max99]
    Opacity: Optional[_integerMin0Max100]
    StartTime: Optional[_stringPattern01D20305D205D]
    Width: Optional[_integerMin0Max2147483647]


_listOfInsertableImage = List[InsertableImage]


class ImageInserter(TypedDict, total=False):
    """Use the image inserter feature to include a graphic overlay on your
    video. Enable or disable this feature for each input or output
    individually. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/graphic-overlay.html.
    This setting is disabled by default.
    """

    InsertableImages: Optional[_listOfInsertableImage]
    SdrReferenceWhiteLevel: Optional[_integerMin100Max1000]


class Hdr10Plus(TypedDict, total=False):
    """Setting for HDR10+ metadata insertion"""

    MasteringMonitorNits: Optional[_integerMin0Max4000]
    TargetMonitorNits: Optional[_integerMin0Max4000]


class DolbyVisionLevel6Metadata(TypedDict, total=False):
    """Use these settings when you set DolbyVisionLevel6Mode to SPECIFY to
    override the MaxCLL and MaxFALL values in your input with new values.
    """

    MaxCll: Optional[_integerMin0Max65535]
    MaxFall: Optional[_integerMin0Max65535]


class DolbyVision(TypedDict, total=False):
    """Create Dolby Vision Profile 5 or Profile 8.1 compatible video output."""

    L6Metadata: Optional[DolbyVisionLevel6Metadata]
    L6Mode: Optional[DolbyVisionLevel6Mode]
    Mapping: Optional[DolbyVisionMapping]
    Profile: Optional[DolbyVisionProfile]


class Deinterlacer(TypedDict, total=False):
    """Settings for deinterlacer"""

    Algorithm: Optional[DeinterlaceAlgorithm]
    Control: Optional[DeinterlacerControl]
    Mode: Optional[DeinterlacerMode]


class VideoPreprocessor(TypedDict, total=False):
    """Find additional transcoding features under Preprocessors. Enable the
    features at each output individually. These features are disabled by
    default.
    """

    ColorCorrector: Optional[ColorCorrector]
    Deinterlacer: Optional[Deinterlacer]
    DolbyVision: Optional[DolbyVision]
    Hdr10Plus: Optional[Hdr10Plus]
    ImageInserter: Optional[ImageInserter]
    NoiseReducer: Optional[NoiseReducer]
    PartnerWatermarking: Optional[PartnerWatermarking]
    TimecodeBurnin: Optional[TimecodeBurnin]


class Rectangle(TypedDict, total=False):
    """Use Rectangle to identify a specific area of the video frame."""

    Height: Optional[_integerMin2Max2147483647]
    Width: Optional[_integerMin2Max2147483647]
    X: Optional[_integerMin0Max2147483647]
    Y: Optional[_integerMin0Max2147483647]


class XavcHdProfileSettings(TypedDict, total=False):
    """Required when you set Profile to the value XAVC_HD."""

    BitrateClass: Optional[XavcHdProfileBitrateClass]
    FlickerAdaptiveQuantization: Optional[XavcFlickerAdaptiveQuantization]
    GopBReference: Optional[XavcGopBReference]
    GopClosedCadence: Optional[_integerMin0Max2147483647]
    HrdBufferSize: Optional[_integerMin0Max1152000000]
    InterlaceMode: Optional[XavcInterlaceMode]
    QualityTuningLevel: Optional[XavcHdProfileQualityTuningLevel]
    Slices: Optional[_integerMin4Max12]
    Telecine: Optional[XavcHdProfileTelecine]


class XavcHdIntraCbgProfileSettings(TypedDict, total=False):
    """Required when you set Profile to the value XAVC_HD_INTRA_CBG."""

    XavcClass: Optional[XavcHdIntraCbgProfileClass]


class Xavc4kProfileSettings(TypedDict, total=False):
    """Required when you set Profile to the value XAVC_4K."""

    BitrateClass: Optional[Xavc4kProfileBitrateClass]
    CodecProfile: Optional[Xavc4kProfileCodecProfile]
    FlickerAdaptiveQuantization: Optional[XavcFlickerAdaptiveQuantization]
    GopBReference: Optional[XavcGopBReference]
    GopClosedCadence: Optional[_integerMin0Max2147483647]
    HrdBufferSize: Optional[_integerMin0Max1152000000]
    QualityTuningLevel: Optional[Xavc4kProfileQualityTuningLevel]
    Slices: Optional[_integerMin8Max12]


class Xavc4kIntraVbrProfileSettings(TypedDict, total=False):
    """Required when you set Profile to the value XAVC_4K_INTRA_VBR."""

    XavcClass: Optional[Xavc4kIntraVbrProfileClass]


class Xavc4kIntraCbgProfileSettings(TypedDict, total=False):
    """Required when you set Profile to the value XAVC_4K_INTRA_CBG."""

    XavcClass: Optional[Xavc4kIntraCbgProfileClass]


class XavcSettings(TypedDict, total=False):
    """Required when you set Codec to the value XAVC."""

    AdaptiveQuantization: Optional[XavcAdaptiveQuantization]
    EntropyEncoding: Optional[XavcEntropyEncoding]
    FramerateControl: Optional[XavcFramerateControl]
    FramerateConversionAlgorithm: Optional[XavcFramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max1001]
    FramerateNumerator: Optional[_integerMin24Max60000]
    PerFrameMetrics: Optional[_listOfFrameMetricType]
    Profile: Optional[XavcProfile]
    SlowPal: Optional[XavcSlowPal]
    Softness: Optional[_integerMin0Max128]
    SpatialAdaptiveQuantization: Optional[XavcSpatialAdaptiveQuantization]
    TemporalAdaptiveQuantization: Optional[XavcTemporalAdaptiveQuantization]
    Xavc4kIntraCbgProfileSettings: Optional[Xavc4kIntraCbgProfileSettings]
    Xavc4kIntraVbrProfileSettings: Optional[Xavc4kIntraVbrProfileSettings]
    Xavc4kProfileSettings: Optional[Xavc4kProfileSettings]
    XavcHdIntraCbgProfileSettings: Optional[XavcHdIntraCbgProfileSettings]
    XavcHdProfileSettings: Optional[XavcHdProfileSettings]


class Vp9Settings(TypedDict, total=False):
    """Required when you set Codec to the value VP9."""

    Bitrate: Optional[_integerMin1000Max480000000]
    FramerateControl: Optional[Vp9FramerateControl]
    FramerateConversionAlgorithm: Optional[Vp9FramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max2147483647]
    FramerateNumerator: Optional[_integerMin1Max2147483647]
    GopSize: Optional[_doubleMin0]
    HrdBufferSize: Optional[_integerMin0Max47185920]
    MaxBitrate: Optional[_integerMin1000Max480000000]
    ParControl: Optional[Vp9ParControl]
    ParDenominator: Optional[_integerMin1Max2147483647]
    ParNumerator: Optional[_integerMin1Max2147483647]
    QualityTuningLevel: Optional[Vp9QualityTuningLevel]
    RateControlMode: Optional[Vp9RateControlMode]


class Vp8Settings(TypedDict, total=False):
    """Required when you set Codec to the value VP8."""

    Bitrate: Optional[_integerMin1000Max1152000000]
    FramerateControl: Optional[Vp8FramerateControl]
    FramerateConversionAlgorithm: Optional[Vp8FramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max2147483647]
    FramerateNumerator: Optional[_integerMin1Max2147483647]
    GopSize: Optional[_doubleMin0]
    HrdBufferSize: Optional[_integerMin0Max47185920]
    MaxBitrate: Optional[_integerMin1000Max1152000000]
    ParControl: Optional[Vp8ParControl]
    ParDenominator: Optional[_integerMin1Max2147483647]
    ParNumerator: Optional[_integerMin1Max2147483647]
    QualityTuningLevel: Optional[Vp8QualityTuningLevel]
    RateControlMode: Optional[Vp8RateControlMode]


class Vc3Settings(TypedDict, total=False):
    """Required when you set Codec to the value VC3"""

    FramerateControl: Optional[Vc3FramerateControl]
    FramerateConversionAlgorithm: Optional[Vc3FramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max1001]
    FramerateNumerator: Optional[_integerMin24Max60000]
    InterlaceMode: Optional[Vc3InterlaceMode]
    ScanTypeConversionMode: Optional[Vc3ScanTypeConversionMode]
    SlowPal: Optional[Vc3SlowPal]
    Telecine: Optional[Vc3Telecine]
    Vc3Class: Optional[Vc3Class]


class UncompressedSettings(TypedDict, total=False):
    """Required when you set Codec, under VideoDescription>CodecSettings to the
    value UNCOMPRESSED.
    """

    Fourcc: Optional[UncompressedFourcc]
    FramerateControl: Optional[UncompressedFramerateControl]
    FramerateConversionAlgorithm: Optional[UncompressedFramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max2147483647]
    FramerateNumerator: Optional[_integerMin1Max2147483647]
    InterlaceMode: Optional[UncompressedInterlaceMode]
    ScanTypeConversionMode: Optional[UncompressedScanTypeConversionMode]
    SlowPal: Optional[UncompressedSlowPal]
    Telecine: Optional[UncompressedTelecine]


class ProresSettings(TypedDict, total=False):
    """Required when you set Codec to the value PRORES."""

    ChromaSampling: Optional[ProresChromaSampling]
    CodecProfile: Optional[ProresCodecProfile]
    FramerateControl: Optional[ProresFramerateControl]
    FramerateConversionAlgorithm: Optional[ProresFramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max2147483647]
    FramerateNumerator: Optional[_integerMin1Max2147483647]
    InterlaceMode: Optional[ProresInterlaceMode]
    ParControl: Optional[ProresParControl]
    ParDenominator: Optional[_integerMin1Max2147483647]
    ParNumerator: Optional[_integerMin1Max2147483647]
    PerFrameMetrics: Optional[_listOfFrameMetricType]
    ScanTypeConversionMode: Optional[ProresScanTypeConversionMode]
    SlowPal: Optional[ProresSlowPal]
    Telecine: Optional[ProresTelecine]


class Mpeg2Settings(TypedDict, total=False):
    """Required when you set Codec to the value MPEG2."""

    AdaptiveQuantization: Optional[Mpeg2AdaptiveQuantization]
    Bitrate: Optional[_integerMin1000Max288000000]
    CodecLevel: Optional[Mpeg2CodecLevel]
    CodecProfile: Optional[Mpeg2CodecProfile]
    DynamicSubGop: Optional[Mpeg2DynamicSubGop]
    FramerateControl: Optional[Mpeg2FramerateControl]
    FramerateConversionAlgorithm: Optional[Mpeg2FramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max1001]
    FramerateNumerator: Optional[_integerMin24Max60000]
    GopClosedCadence: Optional[_integerMin0Max2147483647]
    GopSize: Optional[_doubleMin0]
    GopSizeUnits: Optional[Mpeg2GopSizeUnits]
    HrdBufferFinalFillPercentage: Optional[_integerMin0Max100]
    HrdBufferInitialFillPercentage: Optional[_integerMin0Max100]
    HrdBufferSize: Optional[_integerMin0Max47185920]
    InterlaceMode: Optional[Mpeg2InterlaceMode]
    IntraDcPrecision: Optional[Mpeg2IntraDcPrecision]
    MaxBitrate: Optional[_integerMin1000Max300000000]
    MinIInterval: Optional[_integerMin0Max30]
    NumberBFramesBetweenReferenceFrames: Optional[_integerMin0Max7]
    ParControl: Optional[Mpeg2ParControl]
    ParDenominator: Optional[_integerMin1Max2147483647]
    ParNumerator: Optional[_integerMin1Max2147483647]
    PerFrameMetrics: Optional[_listOfFrameMetricType]
    QualityTuningLevel: Optional[Mpeg2QualityTuningLevel]
    RateControlMode: Optional[Mpeg2RateControlMode]
    ScanTypeConversionMode: Optional[Mpeg2ScanTypeConversionMode]
    SceneChangeDetect: Optional[Mpeg2SceneChangeDetect]
    SlowPal: Optional[Mpeg2SlowPal]
    Softness: Optional[_integerMin0Max128]
    SpatialAdaptiveQuantization: Optional[Mpeg2SpatialAdaptiveQuantization]
    Syntax: Optional[Mpeg2Syntax]
    Telecine: Optional[Mpeg2Telecine]
    TemporalAdaptiveQuantization: Optional[Mpeg2TemporalAdaptiveQuantization]


class H265QvbrSettings(TypedDict, total=False):
    """Settings for quality-defined variable bitrate encoding with the H.265
    codec. Use these settings only when you set QVBR for Rate control mode.
    """

    MaxAverageBitrate: Optional[_integerMin1000Max1466400000]
    QvbrQualityLevel: Optional[_integerMin1Max10]
    QvbrQualityLevelFineTune: Optional[_doubleMin0Max1]


class H265Settings(TypedDict, total=False):
    """Settings for H265 codec"""

    AdaptiveQuantization: Optional[H265AdaptiveQuantization]
    AlternateTransferFunctionSei: Optional[H265AlternateTransferFunctionSei]
    BandwidthReductionFilter: Optional[BandwidthReductionFilter]
    Bitrate: Optional[_integerMin1000Max1466400000]
    CodecLevel: Optional[H265CodecLevel]
    CodecProfile: Optional[H265CodecProfile]
    Deblocking: Optional[H265Deblocking]
    DynamicSubGop: Optional[H265DynamicSubGop]
    EndOfStreamMarkers: Optional[H265EndOfStreamMarkers]
    FlickerAdaptiveQuantization: Optional[H265FlickerAdaptiveQuantization]
    FramerateControl: Optional[H265FramerateControl]
    FramerateConversionAlgorithm: Optional[H265FramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max2147483647]
    FramerateNumerator: Optional[_integerMin1Max2147483647]
    GopBReference: Optional[H265GopBReference]
    GopClosedCadence: Optional[_integerMin0Max2147483647]
    GopSize: Optional[_doubleMin0]
    GopSizeUnits: Optional[H265GopSizeUnits]
    HrdBufferFinalFillPercentage: Optional[_integerMin0Max100]
    HrdBufferInitialFillPercentage: Optional[_integerMin0Max100]
    HrdBufferSize: Optional[_integerMin0Max1466400000]
    InterlaceMode: Optional[H265InterlaceMode]
    MaxBitrate: Optional[_integerMin1000Max1466400000]
    MinIInterval: Optional[_integerMin0Max30]
    NumberBFramesBetweenReferenceFrames: Optional[_integerMin0Max7]
    NumberReferenceFrames: Optional[_integerMin1Max6]
    ParControl: Optional[H265ParControl]
    ParDenominator: Optional[_integerMin1Max2147483647]
    ParNumerator: Optional[_integerMin1Max2147483647]
    PerFrameMetrics: Optional[_listOfFrameMetricType]
    QualityTuningLevel: Optional[H265QualityTuningLevel]
    QvbrSettings: Optional[H265QvbrSettings]
    RateControlMode: Optional[H265RateControlMode]
    SampleAdaptiveOffsetFilterMode: Optional[H265SampleAdaptiveOffsetFilterMode]
    ScanTypeConversionMode: Optional[H265ScanTypeConversionMode]
    SceneChangeDetect: Optional[H265SceneChangeDetect]
    Slices: Optional[_integerMin1Max32]
    SlowPal: Optional[H265SlowPal]
    SpatialAdaptiveQuantization: Optional[H265SpatialAdaptiveQuantization]
    Telecine: Optional[H265Telecine]
    TemporalAdaptiveQuantization: Optional[H265TemporalAdaptiveQuantization]
    TemporalIds: Optional[H265TemporalIds]
    Tiles: Optional[H265Tiles]
    UnregisteredSeiTimecode: Optional[H265UnregisteredSeiTimecode]
    WriteMp4PackagingType: Optional[H265WriteMp4PackagingType]


class H264QvbrSettings(TypedDict, total=False):
    """Settings for quality-defined variable bitrate encoding with the H.264
    codec. Use these settings only when you set QVBR for Rate control mode.
    """

    MaxAverageBitrate: Optional[_integerMin1000Max1152000000]
    QvbrQualityLevel: Optional[_integerMin1Max10]
    QvbrQualityLevelFineTune: Optional[_doubleMin0Max1]


class H264Settings(TypedDict, total=False):
    """Required when you set Codec to the value H_264."""

    AdaptiveQuantization: Optional[H264AdaptiveQuantization]
    BandwidthReductionFilter: Optional[BandwidthReductionFilter]
    Bitrate: Optional[_integerMin1000Max1152000000]
    CodecLevel: Optional[H264CodecLevel]
    CodecProfile: Optional[H264CodecProfile]
    DynamicSubGop: Optional[H264DynamicSubGop]
    EndOfStreamMarkers: Optional[H264EndOfStreamMarkers]
    EntropyEncoding: Optional[H264EntropyEncoding]
    FieldEncoding: Optional[H264FieldEncoding]
    FlickerAdaptiveQuantization: Optional[H264FlickerAdaptiveQuantization]
    FramerateControl: Optional[H264FramerateControl]
    FramerateConversionAlgorithm: Optional[H264FramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max2147483647]
    FramerateNumerator: Optional[_integerMin1Max2147483647]
    GopBReference: Optional[H264GopBReference]
    GopClosedCadence: Optional[_integerMin0Max2147483647]
    GopSize: Optional[_doubleMin0]
    GopSizeUnits: Optional[H264GopSizeUnits]
    HrdBufferFinalFillPercentage: Optional[_integerMin0Max100]
    HrdBufferInitialFillPercentage: Optional[_integerMin0Max100]
    HrdBufferSize: Optional[_integerMin0Max1152000000]
    InterlaceMode: Optional[H264InterlaceMode]
    MaxBitrate: Optional[_integerMin1000Max1152000000]
    MinIInterval: Optional[_integerMin0Max30]
    NumberBFramesBetweenReferenceFrames: Optional[_integerMin0Max7]
    NumberReferenceFrames: Optional[_integerMin1Max6]
    ParControl: Optional[H264ParControl]
    ParDenominator: Optional[_integerMin1Max2147483647]
    ParNumerator: Optional[_integerMin1Max2147483647]
    PerFrameMetrics: Optional[_listOfFrameMetricType]
    QualityTuningLevel: Optional[H264QualityTuningLevel]
    QvbrSettings: Optional[H264QvbrSettings]
    RateControlMode: Optional[H264RateControlMode]
    RepeatPps: Optional[H264RepeatPps]
    SaliencyAwareEncoding: Optional[H264SaliencyAwareEncoding]
    ScanTypeConversionMode: Optional[H264ScanTypeConversionMode]
    SceneChangeDetect: Optional[H264SceneChangeDetect]
    Slices: Optional[_integerMin1Max32]
    SlowPal: Optional[H264SlowPal]
    Softness: Optional[_integerMin0Max128]
    SpatialAdaptiveQuantization: Optional[H264SpatialAdaptiveQuantization]
    Syntax: Optional[H264Syntax]
    Telecine: Optional[H264Telecine]
    TemporalAdaptiveQuantization: Optional[H264TemporalAdaptiveQuantization]
    UnregisteredSeiTimecode: Optional[H264UnregisteredSeiTimecode]
    WriteMp4PackagingType: Optional[H264WriteMp4PackagingType]


class GifSettings(TypedDict, total=False):
    """Required when you set (Codec) under (VideoDescription)>(CodecSettings)
    to the value GIF
    """

    FramerateControl: Optional[GifFramerateControl]
    FramerateConversionAlgorithm: Optional[GifFramerateConversionAlgorithm]
    FramerateDenominator: Optional[_integerMin1Max2147483647]
    FramerateNumerator: Optional[_integerMin1Max2147483647]


class FrameCaptureSettings(TypedDict, total=False):
    """Required when you set Codec to the value FRAME_CAPTURE."""

    FramerateDenominator: Optional[_integerMin1Max2147483647]
    FramerateNumerator: Optional[_integerMin1Max2147483647]
    MaxCaptures: Optional[_integerMin1Max10000000]
    Quality: Optional[_integerMin1Max100]


class VideoCodecSettings(TypedDict, total=False):
    """Video codec settings contains the group of settings related to video
    encoding. The settings in this group vary depending on the value that
    you choose for Video codec. For each codec enum that you choose, define
    the corresponding settings object. The following lists the codec enum,
    settings object pairs. \\* AV1, Av1Settings \\* AVC_INTRA,
    AvcIntraSettings \\* FRAME_CAPTURE, FrameCaptureSettings \\* GIF,
    GifSettings \\* H_264, H264Settings \\* H_265, H265Settings \\* MPEG2,
    Mpeg2Settings \\* PRORES, ProresSettings \\* UNCOMPRESSED,
    UncompressedSettings \\* VC3, Vc3Settings \\* VP8, Vp8Settings \\* VP9,
    Vp9Settings \\* XAVC, XavcSettings
    """

    Av1Settings: Optional[Av1Settings]
    AvcIntraSettings: Optional[AvcIntraSettings]
    Codec: Optional[VideoCodec]
    FrameCaptureSettings: Optional[FrameCaptureSettings]
    GifSettings: Optional[GifSettings]
    H264Settings: Optional[H264Settings]
    H265Settings: Optional[H265Settings]
    Mpeg2Settings: Optional[Mpeg2Settings]
    ProresSettings: Optional[ProresSettings]
    UncompressedSettings: Optional[UncompressedSettings]
    Vc3Settings: Optional[Vc3Settings]
    Vp8Settings: Optional[Vp8Settings]
    Vp9Settings: Optional[Vp9Settings]
    XavcSettings: Optional[XavcSettings]


class VideoDescription(TypedDict, total=False):
    """Settings related to video encoding of your output. The specific video
    settings depend on the video codec that you choose.
    """

    AfdSignaling: Optional[AfdSignaling]
    AntiAlias: Optional[AntiAlias]
    ChromaPositionMode: Optional[ChromaPositionMode]
    CodecSettings: Optional[VideoCodecSettings]
    ColorMetadata: Optional[ColorMetadata]
    Crop: Optional[Rectangle]
    DropFrameTimecode: Optional[DropFrameTimecode]
    FixedAfd: Optional[_integerMin0Max15]
    Height: Optional[_integerMin32Max8192]
    Position: Optional[Rectangle]
    RespondToAfd: Optional[RespondToAfd]
    ScalingBehavior: Optional[ScalingBehavior]
    Sharpness: Optional[_integerMin0Max100]
    TimecodeInsertion: Optional[VideoTimecodeInsertion]
    TimecodeTrack: Optional[TimecodeTrack]
    VideoPreprocessors: Optional[VideoPreprocessor]
    Width: Optional[_integerMin32Max8192]


class HlsSettings(TypedDict, total=False):
    """Settings for HLS output groups"""

    AudioGroupId: Optional[_string]
    AudioOnlyContainer: Optional[HlsAudioOnlyContainer]
    AudioRenditionSets: Optional[_string]
    AudioTrackType: Optional[HlsAudioTrackType]
    DescriptiveVideoServiceFlag: Optional[HlsDescriptiveVideoServiceFlag]
    IFrameOnlyManifest: Optional[HlsIFrameOnlyManifest]
    SegmentModifier: Optional[_string]


class OutputSettings(TypedDict, total=False):
    """Specific settings for this type of output."""

    HlsSettings: Optional[HlsSettings]


_listOfCaptionDescription = List[CaptionDescription]
_listOfAudioDescription = List[AudioDescription]


class Output(TypedDict, total=False):
    """Each output in your job is a collection of settings that describes how
    you want MediaConvert to encode a single output file or stream. For more
    information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/create-outputs.html.
    """

    AudioDescriptions: Optional[_listOfAudioDescription]
    CaptionDescriptions: Optional[_listOfCaptionDescription]
    ContainerSettings: Optional[ContainerSettings]
    Extension: Optional[_stringMax256]
    NameModifier: Optional[_stringMin1Max256]
    OutputSettings: Optional[OutputSettings]
    Preset: Optional[_stringMin0]
    VideoDescription: Optional[VideoDescription]


_listOfOutput = List[Output]
_listOf__stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12 = List[
    _stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12
]


class SpekeKeyProvider(TypedDict, total=False):
    """If your output group type is HLS, DASH, or Microsoft Smooth, use these
    settings when doing DRM encryption with a SPEKE-compliant key provider.
    If your output group type is CMAF, use the SpekeKeyProviderCmaf settings
    instead.
    """

    CertificateArn: Optional[_stringPatternArnAwsUsGovAcm]
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration]
    ResourceId: Optional[_string]
    SystemIds: Optional[_listOf__stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12]
    Url: Optional[_stringPatternHttpsD]


class MsSmoothEncryptionSettings(TypedDict, total=False):
    """If you are using DRM, set DRM System to specify the value
    SpekeKeyProvider.
    """

    SpekeKeyProvider: Optional[SpekeKeyProvider]


class MsSmoothAdditionalManifest(TypedDict, total=False):
    """Specify the details for each additional Microsoft Smooth Streaming
    manifest that you want the service to generate for this output group.
    Each manifest can reference a different subset of outputs in the group.
    """

    ManifestNameModifier: Optional[_stringMin1]
    SelectedOutputs: Optional[_listOf__stringMin1]


_listOfMsSmoothAdditionalManifest = List[MsSmoothAdditionalManifest]


class MsSmoothGroupSettings(TypedDict, total=False):
    """Settings related to your Microsoft Smooth Streaming output package. For
    more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html.
    """

    AdditionalManifests: Optional[_listOfMsSmoothAdditionalManifest]
    AudioDeduplication: Optional[MsSmoothAudioDeduplication]
    Destination: Optional[_stringPatternS3]
    DestinationSettings: Optional[DestinationSettings]
    Encryption: Optional[MsSmoothEncryptionSettings]
    FragmentLength: Optional[_integerMin1Max2147483647]
    FragmentLengthControl: Optional[MsSmoothFragmentLengthControl]
    ManifestEncoding: Optional[MsSmoothManifestEncoding]


class HlsImageBasedTrickPlaySettings(TypedDict, total=False):
    """Tile and thumbnail settings applicable when imageBasedTrickPlay is
    ADVANCED
    """

    IntervalCadence: Optional[HlsIntervalCadence]
    ThumbnailHeight: Optional[_integerMin2Max4096]
    ThumbnailInterval: Optional[_doubleMin0Max2147483647]
    ThumbnailWidth: Optional[_integerMin8Max4096]
    TileHeight: Optional[_integerMin1Max2048]
    TileWidth: Optional[_integerMin1Max512]


class HlsEncryptionSettings(TypedDict, total=False):
    """Settings for HLS encryption"""

    ConstantInitializationVector: Optional[_stringMin32Max32Pattern09aFAF32]
    EncryptionMethod: Optional[HlsEncryptionType]
    InitializationVectorInManifest: Optional[HlsInitializationVectorInManifest]
    OfflineEncrypted: Optional[HlsOfflineEncrypted]
    SpekeKeyProvider: Optional[SpekeKeyProvider]
    StaticKeyProvider: Optional[StaticKeyProvider]
    Type: Optional[HlsKeyProviderType]


class HlsCaptionLanguageMapping(TypedDict, total=False):
    """Caption Language Mapping"""

    CaptionChannel: Optional[_integerMinNegative2147483648Max2147483647]
    CustomLanguageCode: Optional[_stringMin3Max3PatternAZaZ3]
    LanguageCode: Optional[LanguageCode]
    LanguageDescription: Optional[_string]


_listOfHlsCaptionLanguageMapping = List[HlsCaptionLanguageMapping]


class HlsAdditionalManifest(TypedDict, total=False):
    """Specify the details for each additional HLS manifest that you want the
    service to generate for this output group. Each manifest can reference a
    different subset of outputs in the group.
    """

    ManifestNameModifier: Optional[_stringMin1]
    SelectedOutputs: Optional[_listOf__stringMin1]


_listOfHlsAdditionalManifest = List[HlsAdditionalManifest]
_listOfHlsAdMarkers = List[HlsAdMarkers]


class HlsGroupSettings(TypedDict, total=False):
    """Settings related to your HLS output package. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html.
    """

    AdMarkers: Optional[_listOfHlsAdMarkers]
    AdditionalManifests: Optional[_listOfHlsAdditionalManifest]
    AudioOnlyHeader: Optional[HlsAudioOnlyHeader]
    BaseUrl: Optional[_string]
    CaptionLanguageMappings: Optional[_listOfHlsCaptionLanguageMapping]
    CaptionLanguageSetting: Optional[HlsCaptionLanguageSetting]
    CaptionSegmentLengthControl: Optional[HlsCaptionSegmentLengthControl]
    ClientCache: Optional[HlsClientCache]
    CodecSpecification: Optional[HlsCodecSpecification]
    Destination: Optional[_stringPatternS3]
    DestinationSettings: Optional[DestinationSettings]
    DirectoryStructure: Optional[HlsDirectoryStructure]
    Encryption: Optional[HlsEncryptionSettings]
    ImageBasedTrickPlay: Optional[HlsImageBasedTrickPlay]
    ImageBasedTrickPlaySettings: Optional[HlsImageBasedTrickPlaySettings]
    ManifestCompression: Optional[HlsManifestCompression]
    ManifestDurationFormat: Optional[HlsManifestDurationFormat]
    MinFinalSegmentLength: Optional[_doubleMin0Max2147483647]
    MinSegmentLength: Optional[_integerMin0Max2147483647]
    OutputSelection: Optional[HlsOutputSelection]
    ProgramDateTime: Optional[HlsProgramDateTime]
    ProgramDateTimePeriod: Optional[_integerMin0Max3600]
    ProgressiveWriteHlsManifest: Optional[HlsProgressiveWriteHlsManifest]
    SegmentControl: Optional[HlsSegmentControl]
    SegmentLength: Optional[_integerMin1Max2147483647]
    SegmentLengthControl: Optional[HlsSegmentLengthControl]
    SegmentsPerSubdirectory: Optional[_integerMin1Max2147483647]
    StreamInfResolution: Optional[HlsStreamInfResolution]
    TargetDurationCompatibilityMode: Optional[HlsTargetDurationCompatibilityMode]
    TimedMetadataId3Frame: Optional[HlsTimedMetadataId3Frame]
    TimedMetadataId3Period: Optional[_integerMinNegative2147483648Max2147483647]
    TimestampDeltaMilliseconds: Optional[_integerMinNegative2147483648Max2147483647]


class FileGroupSettings(TypedDict, total=False):
    """Settings related to your File output group. MediaConvert uses this group
    of settings to generate a single standalone file, rather than a
    streaming package.
    """

    Destination: Optional[_stringPatternS3]
    DestinationSettings: Optional[DestinationSettings]


class DashIsoImageBasedTrickPlaySettings(TypedDict, total=False):
    """Tile and thumbnail settings applicable when imageBasedTrickPlay is
    ADVANCED
    """

    IntervalCadence: Optional[DashIsoIntervalCadence]
    ThumbnailHeight: Optional[_integerMin1Max4096]
    ThumbnailInterval: Optional[_doubleMin0Max2147483647]
    ThumbnailWidth: Optional[_integerMin8Max4096]
    TileHeight: Optional[_integerMin1Max2048]
    TileWidth: Optional[_integerMin1Max512]


class DashIsoEncryptionSettings(TypedDict, total=False):
    """Specifies DRM settings for DASH outputs."""

    PlaybackDeviceCompatibility: Optional[DashIsoPlaybackDeviceCompatibility]
    SpekeKeyProvider: Optional[SpekeKeyProvider]


class DashAdditionalManifest(TypedDict, total=False):
    """Specify the details for each additional DASH manifest that you want the
    service to generate for this output group. Each manifest can reference a
    different subset of outputs in the group.
    """

    ManifestNameModifier: Optional[_stringMin1]
    SelectedOutputs: Optional[_listOf__stringMin1]


_listOfDashAdditionalManifest = List[DashAdditionalManifest]


class DashIsoGroupSettings(TypedDict, total=False):
    """Settings related to your DASH output package. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html.
    """

    AdditionalManifests: Optional[_listOfDashAdditionalManifest]
    AudioChannelConfigSchemeIdUri: Optional[DashIsoGroupAudioChannelConfigSchemeIdUri]
    BaseUrl: Optional[_string]
    DashIFrameTrickPlayNameModifier: Optional[_stringMin1Max256]
    DashManifestStyle: Optional[DashManifestStyle]
    Destination: Optional[_stringPatternS3]
    DestinationSettings: Optional[DestinationSettings]
    Encryption: Optional[DashIsoEncryptionSettings]
    FragmentLength: Optional[_integerMin1Max2147483647]
    HbbtvCompliance: Optional[DashIsoHbbtvCompliance]
    ImageBasedTrickPlay: Optional[DashIsoImageBasedTrickPlay]
    ImageBasedTrickPlaySettings: Optional[DashIsoImageBasedTrickPlaySettings]
    MinBufferTime: Optional[_integerMin0Max2147483647]
    MinFinalSegmentLength: Optional[_doubleMin0Max2147483647]
    MpdManifestBandwidthType: Optional[DashIsoMpdManifestBandwidthType]
    MpdProfile: Optional[DashIsoMpdProfile]
    PtsOffsetHandlingForBFrames: Optional[DashIsoPtsOffsetHandlingForBFrames]
    SegmentControl: Optional[DashIsoSegmentControl]
    SegmentLength: Optional[_integerMin1Max2147483647]
    SegmentLengthControl: Optional[DashIsoSegmentLengthControl]
    VideoCompositionOffsets: Optional[DashIsoVideoCompositionOffsets]
    WriteSegmentTimelineInRepresentation: Optional[DashIsoWriteSegmentTimelineInRepresentation]


class OutputGroupSettings(TypedDict, total=False):
    """Output Group settings, including type"""

    CmafGroupSettings: Optional[CmafGroupSettings]
    DashIsoGroupSettings: Optional[DashIsoGroupSettings]
    FileGroupSettings: Optional[FileGroupSettings]
    HlsGroupSettings: Optional[HlsGroupSettings]
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettings]
    PerFrameMetrics: Optional[_listOfFrameMetricType]
    Type: Optional[OutputGroupType]


class OutputGroup(TypedDict, total=False):
    """Group of outputs"""

    AutomatedEncodingSettings: Optional[AutomatedEncodingSettings]
    CustomName: Optional[_string]
    Name: Optional[_stringMax2048]
    OutputGroupSettings: Optional[OutputGroupSettings]
    Outputs: Optional[_listOfOutput]


_listOfOutputGroup = List[OutputGroup]


class NielsenNonLinearWatermarkSettings(TypedDict, total=False):
    """Ignore these settings unless you are using Nielsen non-linear
    watermarking. Specify the values that MediaConvert uses to generate and
    place Nielsen watermarks in your output audio. In addition to specifying
    these values, you also need to set up your cloud TIC server. These
    settings apply to every output in your job. The MediaConvert
    implementation is currently with the following Nielsen versions: Nielsen
    Watermark SDK Version 6.0.13 Nielsen NLM Watermark Engine Version 1.3.3
    Nielsen Watermark Authenticator [SID_TIC] Version [7.0.0]
    """

    ActiveWatermarkProcess: Optional[NielsenActiveWatermarkProcessType]
    AdiFilename: Optional[_stringPatternS3]
    AssetId: Optional[_stringMin1Max20]
    AssetName: Optional[_stringMin1Max50]
    CbetSourceId: Optional[_stringPattern0xAFaF0908190908]
    EpisodeId: Optional[_stringMin1Max20]
    MetadataDestination: Optional[_stringPatternS3]
    SourceId: Optional[_integerMin0Max65534]
    SourceWatermarkStatus: Optional[NielsenSourceWatermarkStatusType]
    TicServerUrl: Optional[_stringPatternHttps]
    UniqueTicPerAudioTrack: Optional[NielsenUniqueTicPerAudioTrackType]


class NielsenConfiguration(TypedDict, total=False):
    """Settings for your Nielsen configuration. If you don't do Nielsen
    measurement and analytics, ignore these settings. When you enable
    Nielsen configuration, MediaConvert enables PCM to ID3 tagging for all
    outputs in the job.
    """

    BreakoutCode: Optional[_integerMin0Max0]
    DistributorId: Optional[_string]


class MotionImageInsertionOffset(TypedDict, total=False):
    """Specify the offset between the upper-left corner of the video frame and
    the top left corner of the overlay.
    """

    ImageX: Optional[_integerMin0Max2147483647]
    ImageY: Optional[_integerMin0Max2147483647]


class MotionImageInsertionFramerate(TypedDict, total=False):
    """For motion overlays that don't have a built-in frame rate, specify the
    frame rate of the overlay in frames per second, as a fraction. For
    example, specify 24 fps as 24/1. The overlay frame rate doesn't need to
    match the frame rate of the underlying video.
    """

    FramerateDenominator: Optional[_integerMin1Max17895697]
    FramerateNumerator: Optional[_integerMin1Max2147483640]


class MotionImageInserter(TypedDict, total=False):
    """Overlay motion graphics on top of your video. The motion graphics that
    you specify here appear on all outputs in all output groups. For more
    information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/motion-graphic-overlay.html.
    """

    Framerate: Optional[MotionImageInsertionFramerate]
    Input: Optional[_stringMin14PatternS3Mov09PngHttpsMov09Png]
    InsertionMode: Optional[MotionImageInsertionMode]
    Offset: Optional[MotionImageInsertionOffset]
    Playback: Optional[MotionImagePlayback]
    StartTime: Optional[_stringMin11Max11Pattern01D20305D205D]


class KantarWatermarkSettings(TypedDict, total=False):
    """Use these settings only when you use Kantar watermarking. Specify the
    values that MediaConvert uses to generate and place Kantar watermarks in
    your output audio. These settings apply to every output in your job. In
    addition to specifying these values, you also need to store your Kantar
    credentials in AWS Secrets Manager. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/kantar-watermarking.html.
    """

    ChannelName: Optional[_stringMin1Max20]
    ContentReference: Optional[_stringMin1Max50PatternAZAZ09]
    CredentialsSecretName: Optional[_stringMin1Max2048PatternArnAZSecretsmanagerWD12SecretAZAZ09]
    FileOffset: Optional[_doubleMin0]
    KantarLicenseId: Optional[_integerMin0Max2147483647]
    KantarServerUrl: Optional[_stringPatternHttpsKantarmedia]
    LogDestination: Optional[_stringPatternS3]
    Metadata3: Optional[_stringMin1Max50]
    Metadata4: Optional[_stringMin1Max50]
    Metadata5: Optional[_stringMin1Max50]
    Metadata6: Optional[_stringMin1Max50]
    Metadata7: Optional[_stringMin1Max50]
    Metadata8: Optional[_stringMin1Max50]


class VideoSelector(TypedDict, total=False):
    """Input video selectors contain the video settings for the input. Each of
    your inputs can have up to one video selector.
    """

    AlphaBehavior: Optional[AlphaBehavior]
    ColorSpace: Optional[ColorSpace]
    ColorSpaceUsage: Optional[ColorSpaceUsage]
    EmbeddedTimecodeOverride: Optional[EmbeddedTimecodeOverride]
    Hdr10Metadata: Optional[Hdr10Metadata]
    MaxLuminance: Optional[_integerMin0Max2147483647]
    PadVideo: Optional[PadVideo]
    Pid: Optional[_integerMin1Max2147483647]
    ProgramNumber: Optional[_integerMinNegative2147483648Max2147483647]
    Rotate: Optional[InputRotate]
    SampleRange: Optional[InputSampleRange]


class VideoOverlayPosition(TypedDict, total=False):
    """position of video overlay"""

    Height: Optional[_integerMinNegative1Max2147483647]
    Unit: Optional[VideoOverlayUnit]
    Width: Optional[_integerMinNegative1Max2147483647]
    XPosition: Optional[_integerMinNegative2147483648Max2147483647]
    YPosition: Optional[_integerMinNegative2147483648Max2147483647]


class VideoOverlayTransition(TypedDict, total=False):
    """Specify one or more Transitions for your video overlay. Use Transitions
    to reposition or resize your overlay over time. To use the same position
    and size for the duration of your video overlay: Leave blank. To specify
    a Transition: Enter a value for Start timecode, End Timecode, X
    Position, Y Position, Width, or Height.
    """

    EndPosition: Optional[VideoOverlayPosition]
    EndTimecode: Optional[_stringPattern010920405090509092]
    StartTimecode: Optional[_stringPattern010920405090509092]


_listOfVideoOverlayTransition = List[VideoOverlayTransition]


class VideoOverlayInputClipping(TypedDict, total=False):
    """To transcode only portions of your video overlay, include one input clip
    for each part of your video overlay that you want in your output.
    """

    EndTimecode: Optional[_stringPattern010920405090509092090909]
    StartTimecode: Optional[_stringPattern010920405090509092090909]


_listOfVideoOverlayInputClipping = List[VideoOverlayInputClipping]


class VideoOverlayInput(TypedDict, total=False):
    """Input settings for Video overlay. You can include one or more video
    overlays in sequence at different times that you specify.
    """

    FileInput: Optional[_stringPatternS3Https]
    InputClippings: Optional[_listOfVideoOverlayInputClipping]
    TimecodeSource: Optional[InputTimecodeSource]
    TimecodeStart: Optional[_stringMin11Max11Pattern01D20305D205D]


class VideoOverlayCrop(TypedDict, total=False):
    """Specify a rectangle of content to crop and use from your video overlay's
    input video. When you do, MediaConvert uses the cropped dimensions that
    you specify under X offset, Y offset, Width, and Height.
    """

    Height: Optional[_integerMin0Max2147483647]
    Unit: Optional[VideoOverlayUnit]
    Width: Optional[_integerMin0Max2147483647]
    X: Optional[_integerMin0Max2147483647]
    Y: Optional[_integerMin0Max2147483647]


class VideoOverlay(TypedDict, total=False):
    """Overlay one or more videos on top of your input video. For more
    information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/video-overlays.html
    """

    Crop: Optional[VideoOverlayCrop]
    EndTimecode: Optional[_stringPattern010920405090509092]
    InitialPosition: Optional[VideoOverlayPosition]
    Input: Optional[VideoOverlayInput]
    Playback: Optional[VideoOverlayPlayBackMode]
    StartTimecode: Optional[_stringPattern010920405090509092]
    Transitions: Optional[_listOfVideoOverlayTransition]


_listOfVideoOverlay = List[VideoOverlay]


class InputVideoGenerator(TypedDict, total=False):
    """When you include Video generator, MediaConvert creates a video input
    with black frames. Use this setting if you do not have a video input or
    if you want to add black video frames before, or after, other inputs.
    You can specify Video generator, or you can specify an Input file, but
    you cannot specify both. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/video-generator.html
    """

    Channels: Optional[_integerMin1Max32]
    Duration: Optional[_integerMin50Max86400000]
    FramerateDenominator: Optional[_integerMin1Max1001]
    FramerateNumerator: Optional[_integerMin1Max60000]
    SampleRate: Optional[_integerMin32000Max48000]


_listOf__stringPatternS3ASSETMAPXml = List[_stringPatternS3ASSETMAPXml]


class InputClipping(TypedDict, total=False):
    """To transcode only portions of your input, include one input clip for
    each part of your input that you want in your output. All input clips
    that you specify will be included in every output of the job. For more
    information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html.
    """

    EndTimecode: Optional[_stringPattern010920405090509092090909]
    StartTimecode: Optional[_stringPattern010920405090509092090909]


_listOfInputClipping = List[InputClipping]


class DynamicAudioSelector(TypedDict, total=False):
    """Use Dynamic audio selectors when you do not know the track layout of
    your source when you submit your job, but want to select multiple audio
    tracks. When you include an audio track in your output and specify this
    Dynamic audio selector as the Audio source, MediaConvert creates an
    audio track within that output for each dynamically selected track. Note
    that when you include a Dynamic audio selector for two or more inputs,
    each input must have the same number of audio tracks and audio channels.
    """

    AudioDurationCorrection: Optional[AudioDurationCorrection]
    ExternalAudioFileInput: Optional[_stringPatternS3Https]
    LanguageCode: Optional[LanguageCode]
    Offset: Optional[_integerMinNegative2147483648Max2147483647]
    SelectorType: Optional[DynamicAudioSelectorType]


_mapOfDynamicAudioSelector = Dict[_string, DynamicAudioSelector]


class InputDecryptionSettings(TypedDict, total=False):
    """Settings for decrypting any input files that you encrypt before you
    upload them to Amazon S3. MediaConvert can decrypt files only when you
    use AWS Key Management Service (KMS) to encrypt the data key that you
    use to encrypt your content.
    """

    DecryptionMode: Optional[DecryptionMode]
    EncryptedDecryptionKey: Optional[_stringMin24Max512PatternAZaZ0902]
    InitializationVector: Optional[_stringMin16Max24PatternAZaZ0922AZaZ0916]
    KmsKeyRegion: Optional[_stringMin9Max19PatternAZ26EastWestCentralNorthSouthEastWest1912]


_mapOfCaptionSelector = Dict[_string, CaptionSelector]
_mapOfAudioSelector = Dict[_string, AudioSelector]
_mapOfAudioSelectorGroup = Dict[_string, AudioSelectorGroup]


class Input(TypedDict, total=False):
    """Use inputs to define the source files used in your transcoding job. For
    more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/specify-input-settings.html.
    You can use multiple video inputs to do input stitching. For more
    information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html
    """

    AdvancedInputFilter: Optional[AdvancedInputFilter]
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettings]
    AudioSelectorGroups: Optional[_mapOfAudioSelectorGroup]
    AudioSelectors: Optional[_mapOfAudioSelector]
    CaptionSelectors: Optional[_mapOfCaptionSelector]
    Crop: Optional[Rectangle]
    DeblockFilter: Optional[InputDeblockFilter]
    DecryptionSettings: Optional[InputDecryptionSettings]
    DenoiseFilter: Optional[InputDenoiseFilter]
    DolbyVisionMetadataXml: Optional[_stringMin14PatternS3XmlXMLHttpsXmlXML]
    DynamicAudioSelectors: Optional[_mapOfDynamicAudioSelector]
    FileInput: Optional[_stringMax2048PatternS3Https]
    FilterEnable: Optional[InputFilterEnable]
    FilterStrength: Optional[_integerMin0Max5]
    ImageInserter: Optional[ImageInserter]
    InputClippings: Optional[_listOfInputClipping]
    InputScanType: Optional[InputScanType]
    Position: Optional[Rectangle]
    ProgramNumber: Optional[_integerMin1Max2147483647]
    PsiControl: Optional[InputPsiControl]
    SupplementalImps: Optional[_listOf__stringPatternS3ASSETMAPXml]
    TimecodeSource: Optional[InputTimecodeSource]
    TimecodeStart: Optional[_stringMin11Max11Pattern01D20305D205D]
    VideoGenerator: Optional[InputVideoGenerator]
    VideoOverlays: Optional[_listOfVideoOverlay]
    VideoSelector: Optional[VideoSelector]


_listOfInput = List[Input]


class ExtendedDataServices(TypedDict, total=False):
    """If your source content has EIA-608 Line 21 Data Services, enable this
    feature to specify what MediaConvert does with the Extended Data
    Services (XDS) packets. You can choose to pass through XDS packets, or
    remove them from the output. For more information about XDS, see EIA-608
    Line Data Services, section 9.5.1.5 05h Content Advisory.
    """

    CopyProtectionAction: Optional[CopyProtectionAction]
    VchipAction: Optional[VchipAction]


class EsamSignalProcessingNotification(TypedDict, total=False):
    """ESAM SignalProcessingNotification data defined by
    OC-SP-ESAM-API-I03-131025.
    """

    SccXml: Optional[_stringPatternSNSignalProcessingNotificationNS]


class EsamManifestConfirmConditionNotification(TypedDict, total=False):
    """ESAM ManifestConfirmConditionNotification defined by
    OC-SP-ESAM-API-I03-131025.
    """

    MccXml: Optional[_stringPatternSNManifestConfirmConditionNotificationNS]


class EsamSettings(TypedDict, total=False):
    """Settings for Event Signaling And Messaging (ESAM). If you don't do ad
    insertion, you can ignore these settings.
    """

    ManifestConfirmConditionNotification: Optional[EsamManifestConfirmConditionNotification]
    ResponseSignalPreroll: Optional[_integerMin0Max30000]
    SignalProcessingNotification: Optional[EsamSignalProcessingNotification]


_listOfColorConversion3DLUTSetting = List[ColorConversion3DLUTSetting]


class JobSettings(TypedDict, total=False):
    """JobSettings contains all the transcode settings for a job."""

    AdAvailOffset: Optional[_integerMinNegative1000Max1000]
    AvailBlanking: Optional[AvailBlanking]
    ColorConversion3DLUTSettings: Optional[_listOfColorConversion3DLUTSetting]
    Esam: Optional[EsamSettings]
    ExtendedDataServices: Optional[ExtendedDataServices]
    FollowSource: Optional[_integerMin1Max150]
    Inputs: Optional[_listOfInput]
    KantarWatermark: Optional[KantarWatermarkSettings]
    MotionImageInserter: Optional[MotionImageInserter]
    NielsenConfiguration: Optional[NielsenConfiguration]
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettings]
    OutputGroups: Optional[_listOfOutputGroup]
    TimecodeConfig: Optional[TimecodeConfig]
    TimedMetadataInsertion: Optional[TimedMetadataInsertion]


class HopDestination(TypedDict, total=False):
    """Optional. Configuration for a destination queue to which the job can hop
    once a customer-defined minimum wait time has passed.
    """

    Priority: Optional[_integerMinNegative50Max50]
    Queue: Optional[_string]
    WaitMinutes: Optional[_integer]


_listOfHopDestination = List[HopDestination]


class CreateJobRequest(ServiceRequest):
    AccelerationSettings: Optional[AccelerationSettings]
    BillingTagsSource: Optional[BillingTagsSource]
    ClientRequestToken: Optional[_string]
    HopDestinations: Optional[_listOfHopDestination]
    JobEngineVersion: Optional[_string]
    JobTemplate: Optional[_string]
    Priority: Optional[_integerMinNegative50Max50]
    Queue: Optional[_string]
    Role: _string
    Settings: JobSettings
    SimulateReservedQueue: Optional[SimulateReservedQueue]
    StatusUpdateInterval: Optional[StatusUpdateInterval]
    Tags: Optional[_mapOf__string]
    UserMetadata: Optional[_mapOf__string]


class WarningGroup(TypedDict, total=False):
    """Contains any warning codes and their count for the job."""

    Code: _integer
    Count: _integer


_listOfWarningGroup = List[WarningGroup]
_timestampUnix = datetime


class Timing(TypedDict, total=False):
    """Information about when jobs are submitted, started, and finished is
    specified in Unix epoch format in seconds.
    """

    FinishTime: Optional[_timestampUnix]
    StartTime: Optional[_timestampUnix]
    SubmitTime: Optional[_timestampUnix]


class QueueTransition(TypedDict, total=False):
    """Description of the source and destination queues between which the job
    has moved, along with the timestamp of the move
    """

    DestinationQueue: Optional[_string]
    SourceQueue: Optional[_string]
    Timestamp: Optional[_timestampUnix]


_listOfQueueTransition = List[QueueTransition]


class VideoDetail(TypedDict, total=False):
    """Contains details about the output's video stream"""

    HeightInPx: Optional[_integer]
    WidthInPx: Optional[_integer]


class OutputDetail(TypedDict, total=False):
    """Details regarding output"""

    DurationInMs: Optional[_integer]
    VideoDetails: Optional[VideoDetail]


_listOfOutputDetail = List[OutputDetail]


class OutputGroupDetail(TypedDict, total=False):
    """Contains details about the output groups specified in the job settings."""

    OutputDetails: Optional[_listOfOutputDetail]


_listOfOutputGroupDetail = List[OutputGroupDetail]
_listOf__string = List[_string]


class JobMessages(TypedDict, total=False):
    """Provides messages from the service about jobs that you have already
    successfully submitted.
    """

    Info: Optional[_listOf__string]
    Warning: Optional[_listOf__string]


class Job(TypedDict, total=False):
    """Each job converts an input file into an output file or files. For more
    information, see the User Guide at
    https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
    """

    AccelerationSettings: Optional[AccelerationSettings]
    AccelerationStatus: Optional[AccelerationStatus]
    Arn: Optional[_string]
    BillingTagsSource: Optional[BillingTagsSource]
    ClientRequestToken: Optional[_string]
    CreatedAt: Optional[_timestampUnix]
    CurrentPhase: Optional[JobPhase]
    ErrorCode: Optional[_integer]
    ErrorMessage: Optional[_string]
    HopDestinations: Optional[_listOfHopDestination]
    Id: Optional[_string]
    JobEngineVersionRequested: Optional[_string]
    JobEngineVersionUsed: Optional[_string]
    JobPercentComplete: Optional[_integer]
    JobTemplate: Optional[_string]
    Messages: Optional[JobMessages]
    OutputGroupDetails: Optional[_listOfOutputGroupDetail]
    Priority: Optional[_integerMinNegative50Max50]
    Queue: Optional[_string]
    QueueTransitions: Optional[_listOfQueueTransition]
    RetryCount: Optional[_integer]
    Role: _string
    Settings: JobSettings
    SimulateReservedQueue: Optional[SimulateReservedQueue]
    Status: Optional[JobStatus]
    StatusUpdateInterval: Optional[StatusUpdateInterval]
    Timing: Optional[Timing]
    UserMetadata: Optional[_mapOf__string]
    Warnings: Optional[_listOfWarningGroup]


class CreateJobResponse(TypedDict, total=False):
    Job: Optional[Job]


class InputTemplate(TypedDict, total=False):
    """Specified video input in a template."""

    AdvancedInputFilter: Optional[AdvancedInputFilter]
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettings]
    AudioSelectorGroups: Optional[_mapOfAudioSelectorGroup]
    AudioSelectors: Optional[_mapOfAudioSelector]
    CaptionSelectors: Optional[_mapOfCaptionSelector]
    Crop: Optional[Rectangle]
    DeblockFilter: Optional[InputDeblockFilter]
    DenoiseFilter: Optional[InputDenoiseFilter]
    DolbyVisionMetadataXml: Optional[_stringMin14PatternS3XmlXMLHttpsXmlXML]
    DynamicAudioSelectors: Optional[_mapOfDynamicAudioSelector]
    FilterEnable: Optional[InputFilterEnable]
    FilterStrength: Optional[_integerMin0Max5]
    ImageInserter: Optional[ImageInserter]
    InputClippings: Optional[_listOfInputClipping]
    InputScanType: Optional[InputScanType]
    Position: Optional[Rectangle]
    ProgramNumber: Optional[_integerMin1Max2147483647]
    PsiControl: Optional[InputPsiControl]
    TimecodeSource: Optional[InputTimecodeSource]
    TimecodeStart: Optional[_stringMin11Max11Pattern01D20305D205D]
    VideoOverlays: Optional[_listOfVideoOverlay]
    VideoSelector: Optional[VideoSelector]


_listOfInputTemplate = List[InputTemplate]


class JobTemplateSettings(TypedDict, total=False):
    """JobTemplateSettings contains all the transcode settings saved in the
    template that will be applied to jobs created from it.
    """

    AdAvailOffset: Optional[_integerMinNegative1000Max1000]
    AvailBlanking: Optional[AvailBlanking]
    ColorConversion3DLUTSettings: Optional[_listOfColorConversion3DLUTSetting]
    Esam: Optional[EsamSettings]
    ExtendedDataServices: Optional[ExtendedDataServices]
    FollowSource: Optional[_integerMin1Max150]
    Inputs: Optional[_listOfInputTemplate]
    KantarWatermark: Optional[KantarWatermarkSettings]
    MotionImageInserter: Optional[MotionImageInserter]
    NielsenConfiguration: Optional[NielsenConfiguration]
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettings]
    OutputGroups: Optional[_listOfOutputGroup]
    TimecodeConfig: Optional[TimecodeConfig]
    TimedMetadataInsertion: Optional[TimedMetadataInsertion]


class CreateJobTemplateRequest(ServiceRequest):
    AccelerationSettings: Optional[AccelerationSettings]
    Category: Optional[_string]
    Description: Optional[_string]
    HopDestinations: Optional[_listOfHopDestination]
    Name: _string
    Priority: Optional[_integerMinNegative50Max50]
    Queue: Optional[_string]
    Settings: JobTemplateSettings
    StatusUpdateInterval: Optional[StatusUpdateInterval]
    Tags: Optional[_mapOf__string]


class JobTemplate(TypedDict, total=False):
    """A job template is a pre-made set of encoding instructions that you can
    use to quickly create a job.
    """

    AccelerationSettings: Optional[AccelerationSettings]
    Arn: Optional[_string]
    Category: Optional[_string]
    CreatedAt: Optional[_timestampUnix]
    Description: Optional[_string]
    HopDestinations: Optional[_listOfHopDestination]
    LastUpdated: Optional[_timestampUnix]
    Name: _string
    Priority: Optional[_integerMinNegative50Max50]
    Queue: Optional[_string]
    Settings: JobTemplateSettings
    StatusUpdateInterval: Optional[StatusUpdateInterval]
    Type: Optional[Type]


class CreateJobTemplateResponse(TypedDict, total=False):
    JobTemplate: Optional[JobTemplate]


_listOfCaptionDescriptionPreset = List[CaptionDescriptionPreset]


class PresetSettings(TypedDict, total=False):
    """Settings for preset"""

    AudioDescriptions: Optional[_listOfAudioDescription]
    CaptionDescriptions: Optional[_listOfCaptionDescriptionPreset]
    ContainerSettings: Optional[ContainerSettings]
    VideoDescription: Optional[VideoDescription]


class CreatePresetRequest(ServiceRequest):
    Category: Optional[_string]
    Description: Optional[_string]
    Name: _string
    Settings: PresetSettings
    Tags: Optional[_mapOf__string]


class Preset(TypedDict, total=False):
    """A preset is a collection of preconfigured media conversion settings that
    you want MediaConvert to apply to the output during the conversion
    process.
    """

    Arn: Optional[_string]
    Category: Optional[_string]
    CreatedAt: Optional[_timestampUnix]
    Description: Optional[_string]
    LastUpdated: Optional[_timestampUnix]
    Name: _string
    Settings: PresetSettings
    Type: Optional[Type]


class CreatePresetResponse(TypedDict, total=False):
    Preset: Optional[Preset]


class ReservationPlanSettings(TypedDict, total=False):
    """Details about the pricing plan for your reserved queue. Required for
    reserved queues and not applicable to on-demand queues.
    """

    Commitment: Commitment
    RenewalType: RenewalType
    ReservedSlots: _integer


class CreateQueueRequest(ServiceRequest):
    ConcurrentJobs: Optional[_integer]
    Description: Optional[_string]
    Name: _string
    PricingPlan: Optional[PricingPlan]
    ReservationPlanSettings: Optional[ReservationPlanSettings]
    Status: Optional[QueueStatus]
    Tags: Optional[_mapOf__string]


class ServiceOverride(TypedDict, total=False):
    """A service override applied by MediaConvert to the settings that you have
    configured. If you see any overrides, we recommend that you contact AWS
    Support.
    """

    Message: Optional[_string]
    Name: Optional[_string]
    OverrideValue: Optional[_string]
    Value: Optional[_string]


_listOfServiceOverride = List[ServiceOverride]


class ReservationPlan(TypedDict, total=False):
    """Details about the pricing plan for your reserved queue. Required for
    reserved queues and not applicable to on-demand queues.
    """

    Commitment: Optional[Commitment]
    ExpiresAt: Optional[_timestampUnix]
    PurchasedAt: Optional[_timestampUnix]
    RenewalType: Optional[RenewalType]
    ReservedSlots: Optional[_integer]
    Status: Optional[ReservationPlanStatus]


class Queue(TypedDict, total=False):
    """You can use queues to manage the resources that are available to your
    AWS account for running multiple transcoding jobs at the same time. If
    you don't specify a queue, the service sends all jobs through the
    default queue. For more information, see
    https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html.
    """

    Arn: Optional[_string]
    ConcurrentJobs: Optional[_integer]
    CreatedAt: Optional[_timestampUnix]
    Description: Optional[_string]
    LastUpdated: Optional[_timestampUnix]
    Name: _string
    PricingPlan: Optional[PricingPlan]
    ProgressingJobsCount: Optional[_integer]
    ReservationPlan: Optional[ReservationPlan]
    ServiceOverrides: Optional[_listOfServiceOverride]
    Status: Optional[QueueStatus]
    SubmittedJobsCount: Optional[_integer]
    Type: Optional[Type]


class CreateQueueResponse(TypedDict, total=False):
    Queue: Optional[Queue]


class DeleteJobTemplateRequest(ServiceRequest):
    Name: _string


class DeleteJobTemplateResponse(TypedDict, total=False):
    pass


class DeletePolicyRequest(ServiceRequest):
    pass


class DeletePolicyResponse(TypedDict, total=False):
    pass


class DeletePresetRequest(ServiceRequest):
    Name: _string


class DeletePresetResponse(TypedDict, total=False):
    pass


class DeleteQueueRequest(ServiceRequest):
    Name: _string


class DeleteQueueResponse(TypedDict, total=False):
    pass


class DescribeEndpointsRequest(ServiceRequest):
    MaxResults: Optional[_integer]
    Mode: Optional[DescribeEndpointsMode]
    NextToken: Optional[_string]


class Endpoint(TypedDict, total=False):
    """Describes an account-specific API endpoint."""

    Url: Optional[_string]


_listOfEndpoint = List[Endpoint]


class DescribeEndpointsResponse(TypedDict, total=False):
    Endpoints: Optional[_listOfEndpoint]
    NextToken: Optional[_string]


class DisassociateCertificateRequest(ServiceRequest):
    Arn: _string


class DisassociateCertificateResponse(TypedDict, total=False):
    pass


class ExceptionBody(TypedDict, total=False):
    Message: Optional[_string]


class GetJobRequest(ServiceRequest):
    Id: _string


class GetJobResponse(TypedDict, total=False):
    Job: Optional[Job]


class GetJobTemplateRequest(ServiceRequest):
    Name: _string


class GetJobTemplateResponse(TypedDict, total=False):
    JobTemplate: Optional[JobTemplate]


class GetPolicyRequest(ServiceRequest):
    pass


class Policy(TypedDict, total=False):
    """A policy configures behavior that you allow or disallow for your
    account. For information about MediaConvert policies, see the user guide
    at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
    """

    HttpInputs: Optional[InputPolicy]
    HttpsInputs: Optional[InputPolicy]
    S3Inputs: Optional[InputPolicy]


class GetPolicyResponse(TypedDict, total=False):
    Policy: Optional[Policy]


class GetPresetRequest(ServiceRequest):
    Name: _string


class GetPresetResponse(TypedDict, total=False):
    Preset: Optional[Preset]


class GetQueueRequest(ServiceRequest):
    Name: _string


class GetQueueResponse(TypedDict, total=False):
    Queue: Optional[Queue]


class JobEngineVersion(TypedDict, total=False):
    """Use Job engine versions to run jobs for your production workflow on one
    version, while you test and validate the latest version. Job engine
    versions are in a YYYY-MM-DD format.
    """

    ExpirationDate: Optional[_timestampUnix]
    Version: Optional[_string]


class ListJobTemplatesRequest(ServiceRequest):
    Category: Optional[_string]
    ListBy: Optional[JobTemplateListBy]
    MaxResults: Optional[_integerMin1Max20]
    NextToken: Optional[_string]
    Order: Optional[Order]


_listOfJobTemplate = List[JobTemplate]


class ListJobTemplatesResponse(TypedDict, total=False):
    JobTemplates: Optional[_listOfJobTemplate]
    NextToken: Optional[_string]


class ListJobsRequest(ServiceRequest):
    MaxResults: Optional[_integerMin1Max20]
    NextToken: Optional[_string]
    Order: Optional[Order]
    Queue: Optional[_string]
    Status: Optional[JobStatus]


_listOfJob = List[Job]


class ListJobsResponse(TypedDict, total=False):
    Jobs: Optional[_listOfJob]
    NextToken: Optional[_string]


class ListPresetsRequest(ServiceRequest):
    Category: Optional[_string]
    ListBy: Optional[PresetListBy]
    MaxResults: Optional[_integerMin1Max20]
    NextToken: Optional[_string]
    Order: Optional[Order]


_listOfPreset = List[Preset]


class ListPresetsResponse(TypedDict, total=False):
    NextToken: Optional[_string]
    Presets: Optional[_listOfPreset]


class ListQueuesRequest(ServiceRequest):
    ListBy: Optional[QueueListBy]
    MaxResults: Optional[_integerMin1Max20]
    NextToken: Optional[_string]
    Order: Optional[Order]


_listOfQueue = List[Queue]


class ListQueuesResponse(TypedDict, total=False):
    NextToken: Optional[_string]
    Queues: Optional[_listOfQueue]
    TotalConcurrentJobs: Optional[_integer]
    UnallocatedConcurrentJobs: Optional[_integer]


class ListTagsForResourceRequest(ServiceRequest):
    Arn: _string


class ResourceTags(TypedDict, total=False):
    """The Amazon Resource Name (ARN) and tags for an AWS Elemental
    MediaConvert resource.
    """

    Arn: Optional[_string]
    Tags: Optional[_mapOf__string]


class ListTagsForResourceResponse(TypedDict, total=False):
    ResourceTags: Optional[ResourceTags]


class ListVersionsRequest(ServiceRequest):
    MaxResults: Optional[_integerMin1Max20]
    NextToken: Optional[_string]


_listOfJobEngineVersion = List[JobEngineVersion]


class ListVersionsResponse(TypedDict, total=False):
    NextToken: Optional[_string]
    Versions: Optional[_listOfJobEngineVersion]


class Metadata(TypedDict, total=False):
    """Metadata and other file information."""

    ETag: Optional[_string]
    FileSize: Optional[_long]
    LastModified: Optional[_timestampUnix]
    MimeType: Optional[_string]


class ProbeInputFile(TypedDict, total=False):
    """The input file that needs to be analyzed."""

    FileUrl: Optional[_string]


_listOfProbeInputFile = List[ProbeInputFile]


class ProbeRequest(ServiceRequest):
    InputFiles: Optional[_listOfProbeInputFile]


_listOf__integer = List[_integer]


class TrackMapping(TypedDict, total=False):
    """An array containing track mapping information."""

    AudioTrackIndexes: Optional[_listOf__integer]
    DataTrackIndexes: Optional[_listOf__integer]
    VideoTrackIndexes: Optional[_listOf__integer]


_listOfTrackMapping = List[TrackMapping]


class ProbeResult(TypedDict, total=False):
    """Probe results for your media file."""

    Container: Optional[Container]
    Metadata: Optional[Metadata]
    TrackMappings: Optional[_listOfTrackMapping]


_listOfProbeResult = List[ProbeResult]


class ProbeResponse(TypedDict, total=False):
    ProbeResults: Optional[_listOfProbeResult]


class PutPolicyRequest(ServiceRequest):
    Policy: Policy


class PutPolicyResponse(TypedDict, total=False):
    Policy: Optional[Policy]


class SearchJobsRequest(ServiceRequest):
    InputFile: Optional[_string]
    MaxResults: Optional[_integerMin1Max20]
    NextToken: Optional[_string]
    Order: Optional[Order]
    Queue: Optional[_string]
    Status: Optional[JobStatus]


class SearchJobsResponse(TypedDict, total=False):
    Jobs: Optional[_listOfJob]
    NextToken: Optional[_string]


class TagResourceRequest(ServiceRequest):
    Arn: _string
    Tags: _mapOf__string


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    Arn: _string
    TagKeys: Optional[_listOf__string]


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateJobTemplateRequest(ServiceRequest):
    AccelerationSettings: Optional[AccelerationSettings]
    Category: Optional[_string]
    Description: Optional[_string]
    HopDestinations: Optional[_listOfHopDestination]
    Name: _string
    Priority: Optional[_integerMinNegative50Max50]
    Queue: Optional[_string]
    Settings: Optional[JobTemplateSettings]
    StatusUpdateInterval: Optional[StatusUpdateInterval]


class UpdateJobTemplateResponse(TypedDict, total=False):
    JobTemplate: Optional[JobTemplate]


class UpdatePresetRequest(ServiceRequest):
    Category: Optional[_string]
    Description: Optional[_string]
    Name: _string
    Settings: Optional[PresetSettings]


class UpdatePresetResponse(TypedDict, total=False):
    Preset: Optional[Preset]


class UpdateQueueRequest(ServiceRequest):
    ConcurrentJobs: Optional[_integer]
    Description: Optional[_string]
    Name: _string
    ReservationPlanSettings: Optional[ReservationPlanSettings]
    Status: Optional[QueueStatus]


class UpdateQueueResponse(TypedDict, total=False):
    Queue: Optional[Queue]


_timestampIso8601 = datetime


class MediaconvertApi:
    service = "mediaconvert"
    version = "2017-08-29"

    @handler("AssociateCertificate")
    def associate_certificate(
        self, context: RequestContext, arn: _string, **kwargs
    ) -> AssociateCertificateResponse:
        """Associates an AWS Certificate Manager (ACM) Amazon Resource Name (ARN)
        with AWS Elemental MediaConvert.

        :param arn: The ARN of the ACM certificate that you want to associate with your
        MediaConvert resource.
        :returns: AssociateCertificateResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CancelJob")
    def cancel_job(self, context: RequestContext, id: _string, **kwargs) -> CancelJobResponse:
        """Permanently cancel a job. Once you have canceled a job, you can't start
        it again.

        :param id: The Job ID of the job to be cancelled.
        :returns: CancelJobResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateJob")
    def create_job(
        self,
        context: RequestContext,
        role: _string,
        settings: JobSettings,
        acceleration_settings: AccelerationSettings | None = None,
        billing_tags_source: BillingTagsSource | None = None,
        client_request_token: _string | None = None,
        hop_destinations: _listOfHopDestination | None = None,
        job_engine_version: _string | None = None,
        job_template: _string | None = None,
        priority: _integerMinNegative50Max50 | None = None,
        queue: _string | None = None,
        simulate_reserved_queue: SimulateReservedQueue | None = None,
        status_update_interval: StatusUpdateInterval | None = None,
        tags: _mapOf__string | None = None,
        user_metadata: _mapOf__string | None = None,
        **kwargs,
    ) -> CreateJobResponse:
        """Create a new transcoding job. For information about jobs and job
        settings, see the User Guide at
        http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        :param role: Required.
        :param settings: JobSettings contains all the transcode settings for a job.
        :param acceleration_settings: Optional.
        :param billing_tags_source: Optionally choose a Billing tags source that AWS Billing and Cost
        Management will use to display tags for individual output costs on any
        billing report that you set up.
        :param client_request_token: Prevent duplicate jobs from being created and ensure idempotency for
        your requests.
        :param hop_destinations: Optional.
        :param job_engine_version: Use Job engine versions to run jobs for your production workflow on one
        version, while you test and validate the latest version.
        :param job_template: Optional.
        :param priority: Optional.
        :param queue: Optional.
        :param simulate_reserved_queue: Optional.
        :param status_update_interval: Optional.
        :param tags: Optional.
        :param user_metadata: Optional.
        :returns: CreateJobResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateJobTemplate")
    def create_job_template(
        self,
        context: RequestContext,
        settings: JobTemplateSettings,
        name: _string,
        acceleration_settings: AccelerationSettings | None = None,
        category: _string | None = None,
        description: _string | None = None,
        hop_destinations: _listOfHopDestination | None = None,
        priority: _integerMinNegative50Max50 | None = None,
        queue: _string | None = None,
        status_update_interval: StatusUpdateInterval | None = None,
        tags: _mapOf__string | None = None,
        **kwargs,
    ) -> CreateJobTemplateResponse:
        """Create a new job template. For information about job templates see the
        User Guide at
        http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        :param settings: JobTemplateSettings contains all the transcode settings saved in the
        template that will be applied to jobs created from it.
        :param name: The name of the job template you are creating.
        :param acceleration_settings: Accelerated transcoding can significantly speed up jobs with long,
        visually complex content.
        :param category: Optional.
        :param description: Optional.
        :param hop_destinations: Optional.
        :param priority: Specify the relative priority for this job.
        :param queue: Optional.
        :param status_update_interval: Specify how often MediaConvert sends STATUS_UPDATE events to Amazon
        CloudWatch Events.
        :param tags: The tags that you want to add to the resource.
        :returns: CreateJobTemplateResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreatePreset")
    def create_preset(
        self,
        context: RequestContext,
        settings: PresetSettings,
        name: _string,
        category: _string | None = None,
        description: _string | None = None,
        tags: _mapOf__string | None = None,
        **kwargs,
    ) -> CreatePresetResponse:
        """Create a new preset. For information about job templates see the User
        Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        :param settings: Settings for preset.
        :param name: The name of the preset you are creating.
        :param category: Optional.
        :param description: Optional.
        :param tags: The tags that you want to add to the resource.
        :returns: CreatePresetResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateQueue")
    def create_queue(
        self,
        context: RequestContext,
        name: _string,
        concurrent_jobs: _integer | None = None,
        description: _string | None = None,
        pricing_plan: PricingPlan | None = None,
        reservation_plan_settings: ReservationPlanSettings | None = None,
        status: QueueStatus | None = None,
        tags: _mapOf__string | None = None,
        **kwargs,
    ) -> CreateQueueResponse:
        """Create a new transcoding queue. For information about queues, see
        Working With Queues in the User Guide at
        https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html

        :param name: The name of the queue that you are creating.
        :param concurrent_jobs: Specify the maximum number of jobs your queue can process concurrently.
        :param description: Optional.
        :param pricing_plan: Specifies whether the pricing plan for the queue is on-demand or
        reserved.
        :param reservation_plan_settings: Details about the pricing plan for your reserved queue.
        :param status: Initial state of the queue.
        :param tags: The tags that you want to add to the resource.
        :returns: CreateQueueResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteJobTemplate")
    def delete_job_template(
        self, context: RequestContext, name: _string, **kwargs
    ) -> DeleteJobTemplateResponse:
        """Permanently delete a job template you have created.

        :param name: The name of the job template to be deleted.
        :returns: DeleteJobTemplateResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeletePolicy")
    def delete_policy(self, context: RequestContext, **kwargs) -> DeletePolicyResponse:
        """Permanently delete a policy that you created.

        :returns: DeletePolicyResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeletePreset")
    def delete_preset(
        self, context: RequestContext, name: _string, **kwargs
    ) -> DeletePresetResponse:
        """Permanently delete a preset you have created.

        :param name: The name of the preset to be deleted.
        :returns: DeletePresetResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteQueue")
    def delete_queue(self, context: RequestContext, name: _string, **kwargs) -> DeleteQueueResponse:
        """Permanently delete a queue you have created.

        :param name: The name of the queue that you want to delete.
        :returns: DeleteQueueResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DescribeEndpoints")
    def describe_endpoints(
        self,
        context: RequestContext,
        max_results: _integer | None = None,
        mode: DescribeEndpointsMode | None = None,
        next_token: _string | None = None,
        **kwargs,
    ) -> DescribeEndpointsResponse:
        """Send a request with an empty body to the regional API endpoint to get
        your account API endpoint. Note that DescribeEndpoints is no longer
        required. We recommend that you send your requests directly to the
        regional endpoint instead.

        :param max_results: Optional.
        :param mode: Optional field, defaults to DEFAULT.
        :param next_token: Use this string, provided with the response to a previous request, to
        request the next batch of endpoints.
        :returns: DescribeEndpointsResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DisassociateCertificate")
    def disassociate_certificate(
        self, context: RequestContext, arn: _string, **kwargs
    ) -> DisassociateCertificateResponse:
        """Removes an association between the Amazon Resource Name (ARN) of an AWS
        Certificate Manager (ACM) certificate and an AWS Elemental MediaConvert
        resource.

        :param arn: The ARN of the ACM certificate that you want to disassociate from your
        MediaConvert resource.
        :returns: DisassociateCertificateResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("GetJob")
    def get_job(self, context: RequestContext, id: _string, **kwargs) -> GetJobResponse:
        """Retrieve the JSON for a specific transcoding job.

        :param id: the job ID of the job.
        :returns: GetJobResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("GetJobTemplate")
    def get_job_template(
        self, context: RequestContext, name: _string, **kwargs
    ) -> GetJobTemplateResponse:
        """Retrieve the JSON for a specific job template.

        :param name: The name of the job template.
        :returns: GetJobTemplateResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("GetPolicy")
    def get_policy(self, context: RequestContext, **kwargs) -> GetPolicyResponse:
        """Retrieve the JSON for your policy.

        :returns: GetPolicyResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("GetPreset")
    def get_preset(self, context: RequestContext, name: _string, **kwargs) -> GetPresetResponse:
        """Retrieve the JSON for a specific preset.

        :param name: The name of the preset.
        :returns: GetPresetResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("GetQueue")
    def get_queue(self, context: RequestContext, name: _string, **kwargs) -> GetQueueResponse:
        """Retrieve the JSON for a specific queue.

        :param name: The name of the queue that you want information about.
        :returns: GetQueueResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("ListJobTemplates")
    def list_job_templates(
        self,
        context: RequestContext,
        category: _string | None = None,
        list_by: JobTemplateListBy | None = None,
        max_results: _integerMin1Max20 | None = None,
        next_token: _string | None = None,
        order: Order | None = None,
        **kwargs,
    ) -> ListJobTemplatesResponse:
        """Retrieve a JSON array of up to twenty of your job templates. This will
        return the templates themselves, not just a list of them. To retrieve
        the next twenty templates, use the nextToken string returned with the
        array

        :param category: Optionally, specify a job template category to limit responses to only
        job templates from that category.
        :param list_by: Optional.
        :param max_results: Optional.
        :param next_token: Use this string, provided with the response to a previous request, to
        request the next batch of job templates.
        :param order: Optional.
        :returns: ListJobTemplatesResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("ListJobs")
    def list_jobs(
        self,
        context: RequestContext,
        max_results: _integerMin1Max20 | None = None,
        next_token: _string | None = None,
        order: Order | None = None,
        queue: _string | None = None,
        status: JobStatus | None = None,
        **kwargs,
    ) -> ListJobsResponse:
        """Retrieve a JSON array of up to twenty of your most recently created
        jobs. This array includes in-process, completed, and errored jobs. This
        will return the jobs themselves, not just a list of the jobs. To
        retrieve the twenty next most recent jobs, use the nextToken string
        returned with the array.

        :param max_results: Optional.
        :param next_token: Optional.
        :param order: Optional.
        :param queue: Optional.
        :param status: Optional.
        :returns: ListJobsResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("ListPresets")
    def list_presets(
        self,
        context: RequestContext,
        category: _string | None = None,
        list_by: PresetListBy | None = None,
        max_results: _integerMin1Max20 | None = None,
        next_token: _string | None = None,
        order: Order | None = None,
        **kwargs,
    ) -> ListPresetsResponse:
        """Retrieve a JSON array of up to twenty of your presets. This will return
        the presets themselves, not just a list of them. To retrieve the next
        twenty presets, use the nextToken string returned with the array.

        :param category: Optionally, specify a preset category to limit responses to only presets
        from that category.
        :param list_by: Optional.
        :param max_results: Optional.
        :param next_token: Use this string, provided with the response to a previous request, to
        request the next batch of presets.
        :param order: Optional.
        :returns: ListPresetsResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("ListQueues")
    def list_queues(
        self,
        context: RequestContext,
        list_by: QueueListBy | None = None,
        max_results: _integerMin1Max20 | None = None,
        next_token: _string | None = None,
        order: Order | None = None,
        **kwargs,
    ) -> ListQueuesResponse:
        """Retrieve a JSON array of up to twenty of your queues. This will return
        the queues themselves, not just a list of them. To retrieve the next
        twenty queues, use the nextToken string returned with the array.

        :param list_by: Optional.
        :param max_results: Optional.
        :param next_token: Use this string, provided with the response to a previous request, to
        request the next batch of queues.
        :param order: Optional.
        :returns: ListQueuesResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, arn: _string, **kwargs
    ) -> ListTagsForResourceResponse:
        """Retrieve the tags for a MediaConvert resource.

        :param arn: The Amazon Resource Name (ARN) of the resource that you want to list
        tags for.
        :returns: ListTagsForResourceResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("ListVersions")
    def list_versions(
        self,
        context: RequestContext,
        max_results: _integerMin1Max20 | None = None,
        next_token: _string | None = None,
        **kwargs,
    ) -> ListVersionsResponse:
        """Retrieve a JSON array of all available Job engine versions and the date
        they expire.

        :param max_results: Optional.
        :param next_token: Optional.
        :returns: ListVersionsResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("Probe")
    def probe(
        self, context: RequestContext, input_files: _listOfProbeInputFile | None = None, **kwargs
    ) -> ProbeResponse:
        """Use Probe to obtain detailed information about your input media files.
        Probe returns a JSON that includes container, codec, frame rate,
        resolution, track count, audio layout, captions, and more. You can use
        this information to learn more about your media files, or to help make
        decisions while automating your transcoding workflow.

        :param input_files: Specify a media file to probe.
        :returns: ProbeResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("PutPolicy")
    def put_policy(self, context: RequestContext, policy: Policy, **kwargs) -> PutPolicyResponse:
        """Create or change your policy. For more information about policies, see
        the user guide at
        http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        :param policy: A policy configures behavior that you allow or disallow for your
        account.
        :returns: PutPolicyResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("SearchJobs")
    def search_jobs(
        self,
        context: RequestContext,
        input_file: _string | None = None,
        max_results: _integerMin1Max20 | None = None,
        next_token: _string | None = None,
        order: Order | None = None,
        queue: _string | None = None,
        status: JobStatus | None = None,
        **kwargs,
    ) -> SearchJobsResponse:
        """Retrieve a JSON array that includes job details for up to twenty of your
        most recent jobs. Optionally filter results further according to input
        file, queue, or status. To retrieve the twenty next most recent jobs,
        use the nextToken string returned with the array.

        :param input_file: Optional.
        :param max_results: Optional.
        :param next_token: Optional.
        :param order: Optional.
        :param queue: Optional.
        :param status: Optional.
        :returns: SearchJobsResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, arn: _string, tags: _mapOf__string, **kwargs
    ) -> TagResourceResponse:
        """Add tags to a MediaConvert queue, preset, or job template. For
        information about tagging, see the User Guide at
        https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-resources.html

        :param arn: The Amazon Resource Name (ARN) of the resource that you want to tag.
        :param tags: The tags that you want to add to the resource.
        :returns: TagResourceResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self,
        context: RequestContext,
        arn: _string,
        tag_keys: _listOf__string | None = None,
        **kwargs,
    ) -> UntagResourceResponse:
        """Remove tags from a MediaConvert queue, preset, or job template. For
        information about tagging, see the User Guide at
        https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-resources.html

        :param arn: The Amazon Resource Name (ARN) of the resource that you want to remove
        tags from.
        :param tag_keys: The keys of the tags that you want to remove from the resource.
        :returns: UntagResourceResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateJobTemplate")
    def update_job_template(
        self,
        context: RequestContext,
        name: _string,
        acceleration_settings: AccelerationSettings | None = None,
        category: _string | None = None,
        description: _string | None = None,
        hop_destinations: _listOfHopDestination | None = None,
        priority: _integerMinNegative50Max50 | None = None,
        queue: _string | None = None,
        settings: JobTemplateSettings | None = None,
        status_update_interval: StatusUpdateInterval | None = None,
        **kwargs,
    ) -> UpdateJobTemplateResponse:
        """Modify one of your existing job templates.

        :param name: The name of the job template you are modifying.
        :param acceleration_settings: Accelerated transcoding can significantly speed up jobs with long,
        visually complex content.
        :param category: The new category for the job template, if you are changing it.
        :param description: The new description for the job template, if you are changing it.
        :param hop_destinations: Optional list of hop destinations.
        :param priority: Specify the relative priority for this job.
        :param queue: The new queue for the job template, if you are changing it.
        :param settings: JobTemplateSettings contains all the transcode settings saved in the
        template that will be applied to jobs created from it.
        :param status_update_interval: Specify how often MediaConvert sends STATUS_UPDATE events to Amazon
        CloudWatch Events.
        :returns: UpdateJobTemplateResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdatePreset")
    def update_preset(
        self,
        context: RequestContext,
        name: _string,
        category: _string | None = None,
        description: _string | None = None,
        settings: PresetSettings | None = None,
        **kwargs,
    ) -> UpdatePresetResponse:
        """Modify one of your existing presets.

        :param name: The name of the preset you are modifying.
        :param category: The new category for the preset, if you are changing it.
        :param description: The new description for the preset, if you are changing it.
        :param settings: Settings for preset.
        :returns: UpdatePresetResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateQueue")
    def update_queue(
        self,
        context: RequestContext,
        name: _string,
        concurrent_jobs: _integer | None = None,
        description: _string | None = None,
        reservation_plan_settings: ReservationPlanSettings | None = None,
        status: QueueStatus | None = None,
        **kwargs,
    ) -> UpdateQueueResponse:
        """Modify one of your existing queues.

        :param name: The name of the queue that you are modifying.
        :param concurrent_jobs: Specify the maximum number of jobs your queue can process concurrently.
        :param description: The new description for the queue, if you are changing it.
        :param reservation_plan_settings: The new details of your pricing plan for your reserved queue.
        :param status: Pause or activate a queue by changing its status between ACTIVE and
        PAUSED.
        :returns: UpdateQueueResponse
        :raises BadRequestException:
        :raises InternalServerErrorException:
        :raises ForbiddenException:
        :raises NotFoundException:
        :raises TooManyRequestsException:
        :raises ConflictException:
        """
        raise NotImplementedError
