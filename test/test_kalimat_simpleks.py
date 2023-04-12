import unittest
from cfg_initialization import cfg_true_or_false


class KalimatSimpleksTest(unittest.TestCase):
    """
    Unittest untuk kalimat simpleks (kalimat yang mengandung satu kalimat).

    NOTE:
    - Semua function untuk testcase harus dimulai dengan kata "test".
    - Penambahan '->' pada docstring tiap testcase untuk membuat
      output di terminal mudah dilihat.
    """

    def test_subjek_predikat_01(self):
        """
        -> S-P (nomina-verba)
        (Tersangka, nomina), (bungkam, verba), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<verba>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_02(self):
        """
        -> S-P (nomina-adjektiva)
        (Ia, nomina), (bingung, adjektiva), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<adjektiva>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_03(self):
        """
        -> S-P (nomina-nomina)
        (Ia, nomina), (sekolah, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_04(self):
        """
        -> S-P (nomina-frasaPreposisi)
        (Ia, nomina), (di, preposisi), (pasar, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<preposisi>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_05(self):
        """
        -> S-P (nomina-numeralia)
        (Mereka, nomina), (berdua, numeralia), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<numeralia>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_06(self):
        """
        -> S-P (nomina-frasaNumeralia)
        (Mereka, nomina), (dua, numeralia), (orang, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<numeralia>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_01(self):
        """
        -> S-P-O (frasaNominal-nomina-nomina)
        (Bapak, nomina), (Jokowi, nomina), (seorang, nomina),
        (Presiden, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<nomina>", "<nomina>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_02(self):
        """
        -> S-P-O (nomina-verba-nomina)
        (Presiden, nomina), (memberikan, verba), (grasi, nomina), (., td_akhir_kal)
        """
        kal = ["<nomina>", "<verba>", "<nomina>", "<td_akhir_kal>"]
        self.assertTrue(cfg_true_or_false(kal))

    def test_subjek_predikat_objek_03(self):
        """
        -> S-P-O (nomina-frasaAdjektival-frasaNominal)
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
        -> S-P-O (nomina-frasaPreposisional-frasaNominal)
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
        -> S-P-O (frasaNominal-frasaNumeralia-frasaNominal)
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
