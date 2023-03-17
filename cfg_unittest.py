import nltk
from nltk.parse.chart import SteppingChartParser
from nltk.parse.chart import FilteredBottomUpPredictCombineRule
from nltk.parse.chart import LeafInitRule, FilteredSingleEdgeFundamentalRule
import unittest
import os

model_path = os.path.join(__file__, os.pardir)

grammar = nltk.data.load(
    "file:" + os.path.join(model_path, "utapis_sintaksis_kalimat_v2_skripsi.cfg"), "cfg"
)

LEFT_CORNER_STRATEGY = [
    LeafInitRule(),
    FilteredBottomUpPredictCombineRule(),
    FilteredSingleEdgeFundamentalRule(),
]

utapis_scp = SteppingChartParser(
    grammar=grammar, strategy=LEFT_CORNER_STRATEGY, trace=0
)


def stepping_chart_parsing(scp, tags):
    scp.initialize(tags)

    for step in scp.step():
        # Berhenti bila ditemukan parsing yang lengkap.
        if len(list(scp.parses())) > 0:
            break

        # Berhenti bila sudah tidak ada lagi kemungkinan parsing
        # yang bisa ditambahkan.
        if step is None:
            break

    # Return generator.
    return scp.parses()


def cfg_true_or_false(scp, tags):
    generator = stepping_chart_parsing(scp, tags)
    generator_content_count = len(list(generator))
    if generator_content_count <= 0:
        return False
    else:
        return True


class TestCFG(unittest.TestCase):
    def test_kal_benar_1(self):
        """
        (Tersangka, nomina), (bungkam, verba), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<verba>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_2(self):
        """
        (Ia, nomina), (bingung, adjektiva), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<adjektiva>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_3(self):
        """
        (Bapak, nomina), (Jokowi, nomina), (seorang, nomina),
        (Presiden, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<nomina>", "<nomina>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_4(self):
        """
        (Presiden, nomina), (memberikan, verba), (grasi, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<verba>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_5(self):
        """
        (KPK, nomina), (menangkap, verba), (tersangka, nomina), (di, preposisi),
        (Jakarta, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_6(self):
        """
        (Setiap, numeralia), (warga, nomina), (negara, nomina),
        (berhak, verba), (memperoleh, verba), (pendidikan, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<numeralia>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_7(self):
        """
        (Para, artikel), (hadirin, nomina), (pergi, verba), (menemui, verba),
        (artis, nomina), (tersebut, verba), (di, preposisi), (belakang, nomina),
        (panggung, nomina), (., td_akhir_kal)
        """
        kal = [
            "<artikel>",
            "<nomina>",
            "<verba>",
            "<verba>",
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_8(self):
        """
        (Siapa, nonima), (pun, pun), (harus, adverbia), (siap, verba),
        (dicalonkan, verba), (untuk, konj_sub_tnp_koma_kt_pertama),
        (pilpres, nomina), (2024, numeralia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<pun>",
            "<adverbia>",
            "<verba>",
            "<verba>",
            "<konj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_9(self):
        """
        (Polisi, nomina), (melakukan, verba), (razia, nomina),
        (dua, numeralia), (kali, nomina), (per, artikel),
        (bulan, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<nomina>",
            "<artikel>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_10(self):
        """
        (Dua, numeralia), (per, artikel), (lima, numeralia),
        (dari, preposisi), (hasil, nomina), (voting, nomina),
        (tidak, adverbia), (sah, verba), (., td_akhir_kal)
        """
        kal = [
            "<numeralia>",
            "<artikel>",
            "<numeralia>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_11(self):
        """
        (Polisi, nomina), (melakukan, verba), (pengecekan, nomina),
        (satu, numeralia), (per, artikel), (satu, numeralia),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<artikel>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_12(self):
        """
        (Kejadian, nomina), (itu, nomina), (adalah, verba),
        (insiden, nomina), (tragis, adjektiva),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<adjektiva>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_13(self):
        """
        (Kesehatannya, nomina), (sudah, adverbia), (lebih, adverbia),
        (baik, adjektiva), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<adverbia>", "<adverbia>", "<adjektiva>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_14(self):
        """
        (Kesehatannya, nomina), (sudah, adverbia), (lebih, adverbia), (baik, adjektiva),
        (lagi, adverbia), (., td_akhir_kal).
        """
        kal = [
            "<nomina>",
            "<adverbia>",
            "<adverbia>",
            "<adjektiva>",
            "<adverbia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_15(self):
        """
        (Polisi, nomina), (menemukan, verba), (pisau, nomina),
        (dan, konj_koor_tak_hingga), (senjata, nomina), (api, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<konj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_16(self):
        """
        (Polisi, nomina), (menemukan, verba), (ganja, nomina),
        (,, td_koma), (pisau, nomina), (,, td_koma),
        (dan, konj_koor_tak_hingga), (senjata, nomina),
        (api, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<td_koma>",
            "<konj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_17(self):
        """
        (Polisi, nomina), (tiba, verba), (di, preposisi), (lokasi, nomina),
        (,, td_koma), (tetapi, konj_koor_terhingga), (pencuri, nomina),
        (tersebut, verba), (sudah, adverbia), (pergi, verba),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<td_koma>",
            "<konj_koor_terhingga>",
            "<nomina>",
            "<verba>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_18(self):
        """
        (Telepon, nomina), (seluler, nomina), (,, td_koma), (komputer, nomina),
        (,, td_koma), (atau, konj_koor_tak_hingga), (internet, nomina), (bukan, bukan),
        (barang, nomina), (asing, adjektiva), (lagi, adverbia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<td_koma>",
            "<konj_koor_tak_hingga>",
            "<nomina>",
            "<bukan>",
            "<nomina>",
            "<adjektiva>",
            "<adverbia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_19(self):
        """
        `(Presiden, nomina), (menyatakan, verba), (bahwa, konj_sub_bahwa),
        (reshuffling, nomina), (akan, adverbia), (dilakukan, verba),
        (., td_akhir_kal)`
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<konj_sub_bahwa>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_20(self):
        """
        (Performa, nomina), (perusahaan, nomina), (tahun, nomina),
        (ini, nomina), (lebih, adverbia), (baik, adjektiva), (dari, preposisi),
        (tahun, nomina), (sebelumnya, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<adjektiva>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_21(self):
        """
        (Bangunan, nomina), (ini, nomina), (akan, adverbia),
        (dibuat, verba), (lebih, adverbia), (tinggi, adjektiva),
        (daripada, konj_sub_tnp_koma_kt_pertama), (sebelumnya, nomina),
        (td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<adverbia>",
            "<adjektiva>",
            "<konj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_22(self):
        """
        (Bangunan, nomina), (ini, nomina), (akan, adverbia),
        (dibuat, verba), (lebih, adverbia), (tinggi, adjektiva),
        (dan, konj_koor_tak_hingga), (lebih, adverbia), (besar, adjektiva),
        (daripada, konj_sub_tnp_koma_kt_pertama), (sebelumnya, nomina),
        (td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<adverbia>",
            "<adjektiva>",
            "<konj_koor_tak_hingga>",
            "<adverbia>",
            "<adjektiva>",
            "<konj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_23(self):
        """
        (Pihak, nomina), (kepolisian, nomina), (harus, adverbia),
        (mengusut, verba), (kasus, nomina), (ini, nomina), (dengan, dengan),
        (teliti, adjektiva), (agar, konj_sub_tnp_koma_kt_pertama), (tersangka, nomina),
        (yang, konj_sub_yang), (tidak, adverbia), (pernah, adverbia),
        (tertangkap, verba), (tersebut, verba), (dapat, adverbia), (diadili, verba),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<dengan>",
            "<adjektiva>",
            "<konj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<konj_sub_yang>",
            "<adverbia>",
            "<adverbia>",
            "<verba>",
            "<verba>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_24(self):
        """
        (Gubernur, nomina), (baru, adjektiva), (itu, nomina), (mengatakan, verba),
        (bahwa, konj_sub_bahwa), (dirinya, nomina), (akan, adverbia),
        (bersungguh-sungguh, verba), (bekerja, verba),
        (untuk, konj_sub_tnp_koma_kt_pertama), (rakyat, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adjektiva>",
            "<nomina>",
            "<verba>",
            "<konj_sub_bahwa>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<verba>",
            "<konj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_25(self):
        """
        (Titik, nomina), (kumpul, nomina), (sudah, adverbia), (disepakati, verba),
        (,, td_koma), (yakni, konj_subor), (di, preposisi), (lokasi, nomina),
        (yang, konj_subor), (telah, adverbia), (ditentukan, verba), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<td_koma>",
            "<konj_sub_dgn_koma>",
            "<preposisi>",
            "<nomina>",
            "<konj_sub_yang>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_26(self):
        """
        (Menurut, verba), (UUD, nomina), (1945, numeralia), (,, td_koma),
        (", kutip_awal), (., td_akhir_kal), (", kutip_akhir)
        """
        kal = [
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<td_koma>",
            "<kutip_awal>",
            "<td_akhir_kal>",
            "<kutip_akhir>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_27(self):
        """
        (", kutip_awal), (,, td_koma), (", kutip_akhir), (ujar, verba),
        (para, artikel), (masyarakat, nomina), (., td_akhir_kal)
        """
        kal = [
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<td_koma>",
            "<kutip_awal>",
            "<td_akhir_kal>",
            "<kutip_akhir>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_benar_28(self):
        """
        (Atas, preposisi), (perhatian, nomina), (Saudara, nomina),
        (,, td_koma), (kami, nomina), (ucapkan, verba), (terima, verba),
        (kasih, nomina), (., td_akhir_kal)
        """
        kal = [
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<verba>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_salah_1(self):
        """
        (Tersangka, nomina), (bungkam, verba)
        """
        kal = ["<nomina>", "<verba>"]
        self.assertFalse(cfg_true_or_false(utapis_scp, kal))

    def test_kal_salah_2(self):
        """
        (Polisi, nomina), (tiba, verba), (di, preposisi), (lokasi, nomina),
        (kejadian, nomina), (tetapi, konj_koor_terhingga), (pencuri, nomina),
        (tersebut, verba), (sudah, adverbia), (pergi, verba),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<konj_koor_terhingga>",
            "<nomina>",
            "<verba>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertFalse(cfg_true_or_false(utapis_scp, kal))

    def test_kal_spesial_1(self):
        """
        (Obama, nomina), (menjadi, verba), (presiden, nomina), (Amerika, nomina),
        ('(', kurung_buka), (hal, nomina), (yang, konj_sub_yang), (tidak, adverbia),
        (pernah, adverbia), (terbayangkan, verba), (sebelumnya, nomina), (')',
        kurung_tutup), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<kurung_buka>",
            "<nomina>",
            "<konj_sub_yang>",
            "<adverbia>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<kurung_tutup>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_spesial_2(self):
        """
        (ditambah, verba), (kelalaian, nomina), (protokol, nomina), (kesehatan, nomina),
        (,, td_koma), (pasti, adjektiva), (dapat, adverbia), (menyebabkan, verba),
        (kenaikan, nomina), (covid-19, nomina), (., td_akhir_kal)
        """
        kal = [
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<adjektiva>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_tribun_1(self):
        """
        (Kabid, nomina), (Litbang, nomina), (PP, nomina), (The, nomina),
        (Jakmania, nomina), (,, td_koma), (Afrizal, nomina),
        (Kasriyanto, nomina), (mengatakan, verba), (,, td_koma),
        (The, nomina), (Jakmania, nomina), (yakin, adjektiva),
        (persija, nomina), (bisa, verba), (menang, verba),
        (dari, preposisi), (bali, nomina), (united, nomina),
        (yang, konj_sub_yang), (kini, nomina), (bertengger, verba),
        (di, preposisi), (posisi, nomina), (lima, numeralia),
        (klasemen, nomina), (liga, nomina), (1, numeralia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<adjektiva>",
            "<nomina>",
            "<verba>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<konj_sub_yang>",
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<numeralia>",
            "<nomina>",
            "<nomina>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_tribun_2(self):
        """
        (Evie, nomina), (Masamba, nomina), (dipercaya, verba), (membawakan, verba),
        (lagu, nomina), ('Berakit-akit, nomina), (', simbol), (,, td_koma),
        (diikuti, verba), (oleh, preposisi), (Andmesh, nomina), (dengan, dengan),
        ('Pelangi, nomina), (di, preposisi), (Matamu, nomina), (', simbol), (,, td_koma),
        (dan, konj_koor_tak_hingga), ('Maaf, nomina), (', simbol), (oleh, preposisi),
        (group, nomina), (musik, nomina), (A2L, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<simbol>",
            "<td_koma>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<dengan>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<simbol>",
            "<td_koma>",
            "<konj_koor_tak_hingga>",
            "<nomina>",
            "<simbol>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_tribun_3(self):
        """
        (", kutip_awal), (,, koma), (", kutip_akhir), (kata, verba), (Kabid, nomina),
        (Litbang, nomina), (PP, nomina), (The, nomina), (Jakmania, nomina), (,, td_koma),
        (Afrizal, nomina), (Kasriyanto, nomina), (kepada, preposisi),
        (tribunnews.com, nomina), (,, td_koma), (Jumat, nomina), ('(', kurung buka),
        (26/11/2021, numeralia), (')', kurung tutup), (., td_akhir_kal)
        """
        kal = [
            "<kutip_awal>",
            "<td_koma>",
            "<kutip_akhir>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<kurung_buka>",
            "<numeralia>",
            "<kurung_tutup>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_tribun_4(self):
        """
        (Dirinya, nomina), (tak, adverbia), (mau, adverbia), (ambil, verba),
        (pusing, verba), (,, td_koma), (Ian, nomina), (pun, pun), (siap, verba),
        (melanjutkan, verba), (grup, nomina), (band, nomina), (Radja, nomina),
        (tanpa, konj_sub_tnp_koma_kt_pertama), (adanya, nomina), (dua, numeralia),
        (sahabatnya, nomina), (yang, konj_sub_yang), (telah, adverbia),
        (hengkang, verba), (itu, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adverbia>",
            "<adverbia>",
            "<verba>",
            "<verba>",
            "<td_koma>",
            "<nomina>",
            "<pun>",
            "<verba>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<konj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<numeralia>",
            "<nomina>",
            "<konj_sub_yang>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))

    def test_kal_tribun_5(self):
        """
        (Menurutnya, nomina), (,, td_koma), (perombakan, nomina), (kabinet, nomina),
        (merupakan, verba), (kewenangan, nomina), (Presiden, nomina), (Jokowi, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(utapis_scp, kal))


if __name__ == "__main__":
    unittest.main()
