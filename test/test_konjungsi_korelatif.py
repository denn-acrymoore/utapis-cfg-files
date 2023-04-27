import unittest
from cfg_initialization import cfg_true_or_false


class TestKonjKore(unittest.TestCase):
    def test_lebih_dari_01(self):
        """
        -> S-P-PEL (FN-FADJ-FPREP)
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
        self.assertTrue(cfg_true_or_false(kal))

    def test_lebih_dari_02(self):
        """
        -> S-P-PEL-F_KJ_SUB (FN-FV-FADJ-KJ_SUB-N)
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
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_lebih_dari_03(self):
        """
        -> S-P-PEL-F_KJ_SUB (FN-FV-FADJ-KJ_KOOR-FADJ-KJ_SUB-N)
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
            "<kj_koor_tak_hingga>",
            "<adverbia>",
            "<adjektiva>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_lebih_dari_04(self):
        """
        -> S-P-O-PEL-F_KJ_SUB (FN-[V-V]-FN-KJ_KOOR-FADJ-KJ_SUB-N)
        (Vicky, nomina), (Shu, nomina), (mengaku, verba), (memiliki, verba),
        (tanggung, nomina), (jawab, nomina), (lebih, kj_sub_tnp_koma_kt_pertama),
        (dari, kj_sub_tnp_koma_kt_kedua), (sekadar, adverbia),
        (ibu, nomina), (rumah, nomina), (tangga, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<kj_sub_tnp_koma_kt_kedua>",
            "<adverbia>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_tidak_tetapi_01(self):
        """
        -> Tidak..., tetapi... 01
        (Kita, nomina), (tidak, tidak), (harus, adverbia), (setuju, verba),
        (,, td_koma), (tetapi, kj_koor_terhingga), (harus, adverbia),
        (patuh, adjektiva), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<tidak>",
            "<adverbia>",
            "<verba>",
            "<td_koma>",
            "<kj_koor_terhingga>",
            "<adverbia>",
            "<adjektiva>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_tidak_tetapi_02(self):
        """
        -> Tidak..., tetapi... 02
        (Kita, nomina), (tidak, tidak), (hanya, adverbia), (harus, adverbia),
        (setuju, verba), (,, td_koma), (tetapi, kj_koor_terhingga), (juga, adverbia),
        (harus, adverbia), (lebih, adverbia), (tidak, tidak), (mempertanyakan, verba),
        (putusan, nomina), (itu, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<tidak>",
            "<adverbia>",
            "<adverbia>",
            "<verba>",
            "<td_koma>",
            "<kj_koor_terhingga>",
            "<adverbia>",
            "<adverbia>",
            "<adverbia>",
            "<tidak>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_bukan_melainkan_01(self):
        """
        -> Bukan..., melainkan... 01
        (Bukan, bukan), (masalah, nomina), (itu, nomina),
        (,, td_koma), (melainkan, kj_koor_terhingga_klausa),
        (juga, adverbia), (masalah, nomina), (pendidikan, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<bukan>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<kj_koor_terhingga_klausa>",
            "<adverbia>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_bukan_melainkan_02(self):
        """
        -> Bukan..., melainkan... 02
        (Bukan, bukan), (hanya, adverbia), (masalah, nomina), (itu, nomina),
        (,, td_koma), (melainkan, kj_koor_terhingga_klausa),
        (juga, adverbia), (masalah, nomina), (pendidikan, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<bukan>",
            "<adverbia>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<kj_koor_terhingga_klausa>",
            "<adverbia>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_baik_maupun_01(self):
        """
        -> Baik... maupun... 01
        (Baik, adjektiva), (Pak, nomina), (Anwar, nomina),
        (maupun, kj_koor_tak_hingga), (anaknya, nomina),
        (tidak, tidak), (suka, adjektiva), (merokok, verba),
        (., td_akhir_kal)
        """
        kal = [
            "<adjektiva>",
            "<nomina>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<tidak>",
            "<adjektiva>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_baik_maupun_02(self):
        """
        -> Baik..., ..., maupun... 02
        (Baik, adjektiva), (Anda, nomina), (,, td_koma),
        (istri, nomina), (Anda, nomina), (,, td_koma),
        (maupun, kj_koor_tak_hingga), (mertua, nomina),
        (Anda, nomina), (akan, adverbia), (menerima, verba),
        (cendera, nomina), (mata, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<adjektiva>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_hubungan_dengan_01(self):
        """
        -> Hubungan... dengan... 01
        (Hubungan, nomina), (dia, nomina), (dengan, dengan),
        (adiknya, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<dengan>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_hubungan_dengan_02(self):
        """
        -> Hubungan... dengan... 02
        (Hubungan, nomina), (antara, nomina), (dia, nomina),
        (dengan, dengan), (aku, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<dengan>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_antara_dan_01(self):
        """
        -> Antara... dan... 01
        (Kerajaan, nomina), (itu, nomina), (ditaklukkan, verba),
        (antara, nomina), (tahun, nomina), (1774, numeralia),
        (dan, kj_koor_tak_hingga), (1778, numeralia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<numeralia>",
            "<kj_koor_tak_hingga>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_jangankan_pun_01(self):
        """
        -> Jangankan..., ... pun... 01
        (Jangankan, jangankan), (orang, nomina), (tua, adjektiva),
        (,, td_koma), (orang, nomina), (lain, adjektiva), (pun, pun),
        (harus, adverbia), (dihormati, verba), (., td_akhir_kal)
        """
        kal = [
            "<jangankan>",
            "<nomina>",
            "<adjektiva>",
            "<td_koma>",
            "<nomina>",
            "<adjektiva>",
            "<pun>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_demikian_sehingga_01(self):
        """
        -> Demikian... sehingga... 01
        (Mobil, nomina), (itu, nomina), (larinya, verba),
        (demikian, nomina), (cepatnya, adjektiva),
        (sehingga, kj_sub_tnp_koma_kt_pertama),
        (sangat, adverbia), (sukar, adjektiva),
        (untuk, kj_sub_tnp_koma_kt_pertama), (dipotret, verba)
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<adjektiva>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<adverbia>",
            "<adjektiva>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_sedemikian_rupa_sehingga_01(self):
        """
        -> Sedemikian rupa... sehingga... 01
        (Kita, nomina), (harus, adverbia), (mengerjakannya, verba),
        (sedemikian, nomina), (rupa, nomina), (sehingga, kj_sub_tnp_koma_kt_pertama),
        (hasilnya, nomina), (benar-benar, adjektiva), (baik, adjektiva),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<adjektiva>",
            "<adjektiva>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_entah_entah_01(self):
        """
        -> Entah... entah..., ... 01
        (Entah, entah), (benar, adjektiva), (entah, entah), (tidak, tidak),
        (,, td_koma), (kabar, nomina), (burung, nomina), (itu, nomina),
        (telah, adverbia), (tersebar, verba), (ke, preposisi), (seluruh, numeralia),
        (penduduk, nomina), (desa, nomina), (., td_akhir_kal)
        """
        kal = [
            "<entah>",
            "<adjektiva>",
            "<entah>",
            "<tidak>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<preposisi>",
            "<numeralia>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_entah_entah_02(self):
        """
        -> Entah... entah..., ... 02
        (Entah, entah), (ia, nomina), (sengaja, verba),
        (entah, entah), (ia, nomina), (tidak, tidak),
        (sengaja, verba), (,, td_koma), (ia, nomina),
        (tidak, tidak), (membawa, verba), (buku, nomina),
        (saya, nomina), (., td_akhir_kal)
        """
        kal = [
            "<entah>",
            "<nomina>",
            "<verba>",
            "<entah>",
            "<nomina>",
            "<tidak>",
            "<verba>",
            "<td_koma>",
            "<nomina>",
            "<tidak>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_entah_entah_03(self):
        """
        -> Entah... entah..., ... 03
        (Entah, entah), (karena, kj_sub_tnp_koma_kt_pertama),
        (suka, adjektiva), (entah, entah), (karena, kj_sub_tnp_koma_kt_pertama),
        (lapar, adjektiva), (,, td_koma), (masakan, nomina), (telah, adverbia),
        (dia, nomina), (santap, verba), (hingga, kj_Sub_tnp_koma_kt_pertama),
        (habis, verba), (., td_akhir_kal)
        """
        kal = [
            "<entah>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<adjektiva>",
            "<entah>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<adjektiva>",
            "<td_koma>",
            "<nomina>",
            "<adverbia>",
            "<nomina>",
            "<verba>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_entah_entah_04(self):
        """
        -> Entah... entah..., ... 04
        (Entah, entah), (disetujui, verba), (entah, entah),
        (tidak, tidak), (,, td_koma), (dia, nomina), (tetap, adverbia),
        (akan, adverbia), (mengusulkan, verba), (gagasannya, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<entah>",
            "<verba>",
            "<entah>",
            "<tidak>",
            "<td_koma>",
            "<nomina>",
            "<adverbia>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_apakah_atau_01(self):
        """
        -> Apakah... atau... 01
        (Aku, nomina), (tidak, tidak), (tahu, verba),
        (barang, nomina), (kesukaannya, nomina), (,, td_koma),
        (apakah, nomina), (buku, nomina), (atau, kj_koor_tak_hingga),
        (tas, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<tidak>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_apakah_atau_02(self):
        """
        -> Apa... atau... 02
        (Aku, nomina), (tidak, tidak), (tahu, verba),
        (barang, nomina), (kesukaannya, nomina), (,, td_koma),
        (apa, nomina), (buku, nomina), (atau, kj_koor_tak_hingga),
        (tas, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<tidak>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))
