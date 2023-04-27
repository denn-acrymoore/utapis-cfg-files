import unittest
from cfg_initialization import cfg_true_or_false


class TestKalimatSimpleks(unittest.TestCase):
    """
    Unittest untuk kalimat simpleks (kalimat yang mengandung satu kalimat).

    NOTE:
    - Semua function untuk testcase harus dimulai dengan kata "test".
    - Penambahan '->' pada docstring tiap testcase untuk membuat
      output di terminal mudah dilihat.
    """

    def test_subjek_predikat_01(self):
        """
        -> S-P (N-V)
        (Tersangka, nomina), (bungkam, verba), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<verba>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_02(self):
        """
        -> S-P (N-ADJ)
        (Ia, nomina), (bingung, adjektiva), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<adjektiva>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_03(self):
        """
        -> S-P (N-N)
        (Ia, nomina), (sekolah, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_04(self):
        """
        -> S-P (N-FPREP)
        (Ia, nomina), (di, preposisi), (pasar, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<preposisi>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_05(self):
        """
        -> S-P (N-NUM)
        (Mereka, nomina), (berdua, numeralia), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<numeralia>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_06(self):
        """
        -> S-P (N-FNUM)
        (Mereka, nomina), (dua, numeralia), (orang, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<numeralia>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_07(self):
        """
        -> S-P (N-[ADV-ADV-ADJ])
        (Kesehatannya, nomina), (sudah, adverbia), (lebih, adverbia),
        (baik, adjektiva), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<adverbia>", "<adverbia>", "<adjektiva>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_08(self):
        """
        -> S-P (N-[ADV-ADV-ADJ-ADV])
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
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_01(self):
        """
        -> S-P-O (FN-N-N)
        (Bapak, nomina), (Jokowi, nomina), (seorang, nomina),
        (Presiden, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<nomina>", "<nomina>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_02(self):
        """
        -> S-P-O (N-V-N)
        (Presiden, nomina), (memberikan, verba), (grasi, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<verba>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_03(self):
        """
        -> S-P-O (N-FADJ-FN)
        (Ia, nomina), (sangat, adverbia), (suka, adjektiva),
        (ikan, nomina), (goreng, verba), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adverbia>",
            "<adjektiva>",
            "<nomina>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_04(self):
        """
        -> S-P-O (N-FPREP-FN)
        (Ia, nomina), (sedang, adverbia), (ke, preposisi),
        (taman, nomina), (kota, nomina), (lagi, adverbia),
        (hari, nomina), (ini, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adverbia>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_05(self):
        """
        -> S-P-O (FN-FNUM-FN)
        (Anak, nomina), (Pak, nomina), (Amin, nomina),
        (sepuluh, numeralia), (ekor, nomina),
        (saat, nomina), (ini, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<numeralia>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_06(self):
        """
        -> S-P-O (FNUM-[V-V]-N)
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
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_07(self):
        """
        -> S-P-O (FN-V-FN)
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
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_pelengkap_01(self):
        """
        -> S-P-PEL (FNUM-FPREP-FV)
        (Dua, numeralia), (per, artikel), (lima, numeralia),
        (dari, preposisi), (hasil, nomina), (voting, nomina),
        (tidak, tidak), (sah, verba), (., td_akhir_kal)
        """
        kal = [
            "<numeralia>",
            "<per>",
            "<numeralia>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<tidak>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_pelengkap_02(self):
        """
        -> S-P-PEL_KLAUSA (N-FV-[FN-FV-FPREP])
        (Dia, nomina), (sering, adverbia), (bertanya, verba), (kapan, nomina),
        (kita, nomina), (akan, adverbia), (bertemu, verba), (lagi, adverbia),
        (di, preposisi), (taman, nomina), (., td_akhir_kal).
        """
        kal = [
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<adverbia>",
            "<preposisi>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_pelengkap_01(self):
        """
        -> S-P-O-PEL (FN-FV-FN-FP)
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
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_pelengkap_02(self):
        """
        -> S-P-O-PEL ([A-N]-[V-V]-FN-FPREP)
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
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_pelengkap_03(self):
        """
        -> S-P-O-PEL (N-V-N-FNUM)
        (Polisi, nomina), (melakukan, verba), (razia, nomina),
        (dua, numeralia), (kali, nomina), (per, per),
        (bulan, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<nomina>",
            "<per>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_pelengkap_04(self):
        """
        -> S-P-O-PEL (N-V-N-FNUM)
        (Polisi, nomina), (melakukan, verba), (pengecekan, nomina),
        (satu, numeralia), (per, artikel), (satu, numeralia),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<per>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_salah_subjek_predikat_01(self):
        """
        -> Test: tidak ada 'tanda akhir kal'.
        (Tersangka, nomina), (bungkam, verba)
        """
        kal = ["<nomina>", "<verba>"]
        self.assertFalse(cfg_true_or_false(kal))
