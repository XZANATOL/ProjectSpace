import {useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import "katex/dist/katex.min.css"
import {Button, ButtonGroup, Center, Code, Flex, Heading, Input, Link, ListItem, OrderedList, Text, UnorderedList, VStack, useColorMode} from "@chakra-ui/react"
import ReactMarkdown from "react-markdown"
import {Prism} from "react-syntax-highlighter"
import remarkMath from "remark-math"
import remarkGfm from "remark-gfm"
import rehypeKatex from "rehype-katex"
import rehypeRaw from "rehype-raw"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [state, setState] = useState({"done": "", "text": "", "todos": "", "events": [{"name": "state.hydrate"}]})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const { colorMode, toggleColorMode } = useColorMode()
const Event = events => setState({
  ...state,
  events: [...state.events, ...events],
})
useEffect(() => {
  if(!isReady) {
    return;
  }
  if (!socket.current) {
    connect(socket, state, setState, result, setResult, router, EVENT, ['websocket', 'polling'])
  }
  const update = async () => {
    if (result.state != null) {
      setState({
        ...result.state,
        events: [...state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(state, setState, result, setResult, router, socket.current)
  }
  update()
})
return (
<Flex align="center"
justify="space-around"
sx={{"paddingTop": "10%"}}><VStack sx={{"marginLeft": "2%", "marginRight": "1%", "borderRadius": "md", "border": "1px solid black", "padding": "16px", "width": "100%"}}><Heading size="lg"
sx={{"textDecoration": "underline"}}>{`To-Do`}</Heading>
<ReactMarkdown components={{"h1": ({node, ...props}) => <Heading size='2xl' {...props} />, "h2": ({node, ...props}) => <Heading size='xl' {...props} />, "h3": ({node, ...props}) => <Heading size='lg' {...props} />, "ul": UnorderedList, "ol": OrderedList, "li": ListItem, "p": Text, "a": Link, "code": ({node, inline, className, children, ...props}) =>                      {         const match = (className || '').match(/language-(?<lang>.*)/);         return !inline ? (           <Prism             children={String(children).replace(/ $/, '')}             language={match ? match[1] : ''}             {...props}           />         ) : (           <Code {...props}>             {children}           </Code>         );       }}}
remarkPlugins={[remarkMath, remarkGfm]}
rehypePlugins={[rehypeKatex, rehypeRaw]}>{state.todos}</ReactMarkdown>
<Center sx={{"width": "100%"}}><Input type="text"
placeholder="New record..."
onChange={(_e) => Event([E("state.set_record", {text:_e.target.value})])}
sx={{"width": "50%"}}/>
<ButtonGroup sx={{"marginLeft": "8px"}}><Button onClick={() => Event([E("state.add_record_todo", {})])}
sx={{"borderRadius": "1em"}}>{`Add`}</Button></ButtonGroup></Center></VStack>
<VStack sx={{"marginLeft": "1%", "marginRight": "2%", "borderRadius": "md", "border": "1px solid black", "padding": "16px", "width": "100%"}}><Heading size="lg"
sx={{"textDecoration": "underline"}}>{`Done`}</Heading>
<ReactMarkdown components={{"h1": ({node, ...props}) => <Heading size='2xl' {...props} />, "h2": ({node, ...props}) => <Heading size='xl' {...props} />, "h3": ({node, ...props}) => <Heading size='lg' {...props} />, "ul": UnorderedList, "ol": OrderedList, "li": ListItem, "p": Text, "a": Link, "code": ({node, inline, className, children, ...props}) =>                      {         const match = (className || '').match(/language-(?<lang>.*)/);         return !inline ? (           <Prism             children={String(children).replace(/ $/, '')}             language={match ? match[1] : ''}             {...props}           />         ) : (           <Code {...props}>             {children}           </Code>         );       }}}
remarkPlugins={[remarkMath, remarkGfm]}
rehypePlugins={[rehypeKatex, rehypeRaw]}>{state.done}</ReactMarkdown>
<Center sx={{"width": "100%"}}><Input type="text"
placeholder="New record..."
onChange={(_e) => Event([E("state.set_record", {text:_e.target.value})])}
sx={{"width": "50%"}}/>
<ButtonGroup sx={{"marginLeft": "8px"}}><Button onClick={() => Event([E("state.add_record_done", {})])}
sx={{"borderRadius": "1em"}}>{`Add`}</Button></ButtonGroup></Center></VStack>
<NextHead><title>{`PyneCone_Explore`}</title>
<meta content="A Pynecone app."
name="description"/>
<meta property="og:image"
content="favicon.ico"/></NextHead></Flex>
)
}