# 2. Historical Background

**Part:** 1 — Philosophy  
**Status:** Draft Rev003  
**Type:** Informative  
**Citation Policy:** Informative references included; references should be reviewed before stabilization

Information processing technologies have evolved by addressing different aspects of human intellectual work.

IdeaMark should be understood as a conservative extension of this history rather than a rejection of previous approaches. It does not claim that earlier approaches were wrong. Instead, it assumes that each generation of information technology solved important problems within its own historical and technical constraints.

The purpose of this section is to position IdeaMark within that accumulated history.

## 2.1 Knowledge-Based Systems

Knowledge-based systems attempted to encode expert knowledge explicitly and derive conclusions through inference.

Representative systems such as MYCIN demonstrated that rule-based systems could capture specialized expertise and use it to support reasoning in a bounded domain (Shortliffe, 1976; Buchanan & Shortliffe, 1984).

Industrial systems such as R1/XCON further demonstrated that rule-based systems could be deployed for practical configuration tasks. XCON configured VAX computer systems at Digital Equipment Corporation and became one of the most influential examples of commercial expert systems (McDermott, 1982).

These systems established the importance of explicit knowledge representation. They also exposed a persistent engineering problem: acquiring, formalizing, maintaining, and extending expert knowledge required substantial human effort. This difficulty became widely known as the knowledge acquisition bottleneck.

From the perspective of IdeaMark, knowledge-based systems are important because they show both the power and the cost of attempting to make knowledge explicit.

IdeaMark inherits the ambition of knowledge engineering: to make prior expertise reusable. However, it does not attempt to preserve expert knowledge as fixed rules. Instead, it preserves reusable access structures that allow future intellectual activities to be reconstructed from original sources.

## 2.2 Information Retrieval

Information Retrieval shifted the central problem from representing knowledge to locating relevant information.

Rather than requiring knowledge to be formalized in advance, IR systems made large document collections searchable through indexing, ranking, and query processing. Classical IR research developed models and systems for representing documents and queries, matching them, and ranking results according to relevance (Salton, 1989; van Rijsbergen, 1979; Manning, Raghavan, & Schuetze, 2008).

In practical retrieval systems, inverted indexes became a fundamental structure for scalable document search. By mapping terms to documents or positions, inverted indexes allowed retrieval systems to avoid scanning every document for every query.

The emergence of Web search further changed the scale and social role of retrieval. Brin and Page's work on Google combined large-scale Web crawling, indexing, and link analysis, demonstrating that retrieval could operate over the open Web and become a primary interface to information (Brin & Page, 1998).

Information Retrieval therefore made information vastly more accessible. However, the primary retrieval target remained the document or document fragment. The system could help users find potentially relevant material, but interpretation was still largely performed by the user.

From the perspective of IdeaMark, IR is important because it demonstrates the value of indexing as an access technology. IdeaMark adopts the indexing intuition, but changes the target of reuse from documents to reusable structures of intellectual activity.

## 2.3 Semantic Retrieval

Semantic and dense retrieval methods extended document discovery beyond exact keyword matching.

Traditional sparse retrieval methods such as TF-IDF and BM25 are highly effective but are strongly tied to term occurrence and lexical matching. Dense retrieval methods instead represent questions, passages, or documents as learned vectors and retrieve items according to similarity in that representation space.

Dense Passage Retrieval is a representative example. Karpukhin et al. showed that dense representations learned with a dual-encoder architecture could improve open-domain question answering retrieval performance compared with a strong BM25 baseline (Karpukhin et al., 2020).

Dense retrieval made it possible to retrieve conceptually related passages even when queries and documents used different surface vocabulary. It therefore improved access to relevant documents and fragments under more flexible semantic conditions.

However, the primary retrieval object generally remained the document, passage, or chunk. The system improved semantic matching, but it did not directly represent the intellectual activity that made a source reusable in a future situation.

From the perspective of IdeaMark, semantic retrieval is important because it expands the search surface from lexical matching to representational similarity. IdeaMark is compatible with semantic retrieval, but it introduces another target: reusable traces of intellectual activity anchored to original sources.

## 2.4 Large Language Models

Large Language Models introduced dynamic interpretation, summarization, explanation, translation, and generation.

The Transformer architecture made attention-based sequence modeling a scalable foundation for many language tasks (Vaswani et al., 2017). Later large language models showed that sufficiently scaled pretrained models could perform many tasks from instructions and examples expressed in natural language (Brown et al., 2020).

This development shifted attention from retrieving documents toward generating situation-specific language outputs. LLMs can interpret retrieved materials, transform them into explanations, adapt them to audiences, and combine them with user context.

Retrieval-Augmented Generation connected retrieval and generation by combining parametric memory in pretrained models with non-parametric memory in an external document index. Lewis et al. emphasized that access to explicit non-parametric memory can improve knowledge-intensive tasks and can also support provenance and updating of world knowledge (Lewis et al., 2020).

From the perspective of IdeaMark, LLMs are important because they make dynamic reconstruction of meaning operationally practical. IdeaMark assumes that future interpretation may be performed by humans, AI, or both together.

However, LLMs still need reliable access to authoritative original sources and suitable context for interpretation. IdeaMark contributes by providing reusable structures that help retrieval and interpretation begin from meaningful intellectual activity traces rather than from raw documents alone.

## 2.5 Historical Limitations

Each generation addressed the principal limitation of its predecessor while changing the primary object of computation.

Knowledge-based systems demonstrated that explicit knowledge could be represented and reasoned about within bounded domains. Their limitation was not lack of ambition, but the cost of acquiring, maintaining, and extending formalized knowledge.

Information Retrieval avoided the need to formalize all knowledge by making documents searchable at scale. Its limitation was that retrieved documents still required interpretation before they could support action.

Semantic retrieval reduced dependence on exact terminology by using learned representations and similarity search. Its limitation was that the retrieval object usually remained the document, passage, or chunk rather than the reusable intellectual activity represented through those materials.

Large Language Models made dynamic interpretation and generation practical. Their limitation is not that they cannot generate useful explanations, but that high-quality interpretation depends on access to authoritative sources, appropriate context, and mechanisms for traceability.

These limitations should not be understood as failures.

They are boundaries of successful technologies.

Each technology remains valuable within its intended scope.

## 2.6 Why Another Layer?

IdeaMark does not replace previous generations.

Instead, it introduces a complementary architectural layer.

Previous generations primarily changed what computers process:

- knowledge-based systems process explicit knowledge,
- information retrieval systems process documents and queries,
- semantic retrieval systems process learned representations,
- large language models process and generate language.

IdeaMark changes what can be reused.

It treats reusable intellectual activity structures as first-class objects. These structures connect future situations and projections to authoritative original sources.

This shift is important because AI-enabled systems should not merely produce answers that humans passively accept. If human participants stop thinking, interpreting, acting, and producing new intellectual activities, the shared knowledge environment between humans and AI becomes less capable of growth.

This specification therefore assumes that sustainable AI-enabled knowledge work requires continuous co-evolution between humans and AI.

In this context, co-evolution means the continuous mutual development of humans and AI through shared intellectual activities grounded in authoritative original sources.

IdeaMark supports this co-evolution by making prior intellectual activities discoverable and reusable without fixing a single interpretation in advance. It helps humans and AI find where meaningful thinking can begin, return to authoritative sources, reconstruct meaning under new situations, and produce new intellectual activities that may themselves become future sources.

It is not a new claim that computers can process knowledge, documents, representations, or language.

The proposal is that AI-enabled systems can benefit from reusable indexes of intellectual activity: structures that preserve how an original source can become useful again under a new situation while keeping humans engaged as active interpreters and contributors.

## 2.7 Summary

The historical progression can be summarized as follows:

| Generation | Primary Object | Main Contribution | Remaining Boundary |
| --- | --- | --- | --- |
| Knowledge-Based Systems | Explicit knowledge | Reasoning over formalized expert knowledge | Knowledge acquisition and maintenance cost |
| Information Retrieval | Documents | Scalable discovery of relevant documents | Human interpretation still required |
| Semantic Retrieval | Representations / passages | Similarity-based discovery beyond keywords | Retrieval object remains document-like |
| Large Language Models | Language / interpretation | Dynamic generation and explanation | Requires grounding, context, and traceability |
| IdeaMark | Intellectual activity structures | Reusable access to meaning through original sources | Projection and authoring practices must mature |

IdeaMark is therefore best understood as a conservative but distinct architectural extension.

It preserves continuity with prior work while shifting the object of reuse from knowledge, documents, or generated answers to reusable structures that enable future intellectual activities and human-AI co-evolution.

## Informative References

- Brin, S., & Page, L. (1998). *The Anatomy of a Large-Scale Hypertextual Web Search Engine*. Computer Networks and ISDN Systems, 30(1-7), 107-117.
- Brown, T. B., et al. (2020). *Language Models are Few-Shot Learners*. Advances in Neural Information Processing Systems 33.
- Buchanan, B. G., & Shortliffe, E. H. (Eds.). (1984). *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*. Addison-Wesley.
- Karpukhin, V., Oguz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W. (2020). *Dense Passage Retrieval for Open-Domain Question Answering*. EMNLP 2020.
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Kuttler, H., Lewis, M., Yih, W., Rocktaschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020.
- Manning, C. D., Raghavan, P., & Schuetze, H. (2008). *Introduction to Information Retrieval*. Cambridge University Press.
- McDermott, J. (1982). *R1: A Rule-Based Configurer of Computer Systems*. Artificial Intelligence, 19(1), 39-88.
- Salton, G. (1989). *Automatic Text Processing: The Transformation, Analysis, and Retrieval of Information by Computer*. Addison-Wesley.
- Shortliffe, E. H. (1976). *Computer-Based Medical Consultations: MYCIN*. Elsevier/North-Holland.
- van Rijsbergen, C. J. (1979). *Information Retrieval* (2nd ed.). Butterworths.
- Vaswani, A., et al. (2017). *Attention Is All You Need*. Advances in Neural Information Processing Systems 30.
